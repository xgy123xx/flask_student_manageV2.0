import pymysql
import hashlib
"""
create database students_infov2;
create table student_info(
id int unsigned primary key  auto_increment,
user varchar(20) not null,
pwd char(32) not null,
gender enum('female','male') not null,
score int default 0
);
alter table student_info modify pwd char(32) not null;
alter table student_info modify age score int default 0;
"""
class mysqlHandler:

    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1",user="root",password="123",database="students_infov2",charset="utf8",autocommit=True)
        self.cursor = self.conn.cursor()
        print("connect successed")

    def read(self):
        sql = "SELECT id,user,pwd,gender,score FROM STUDENT_INFO; "
        res = self.cursor.execute(sql)
        students_dt = self.cursor.fetchall()
        return students_dt

    def write(self,student_info):
        #[1, 'alex1', '123456', '1', '33']
        sql = "INSERT INTO student_info(id,user,pwd,gender,score) VALUES(%s,%s,%s,%s,%s); "
        md5 = hashlib.md5()
        md5.update(student_info[2].encode("utf8"))
        student_info[2] = md5.hexdigest()
        res = self.cursor.execute(sql,student_info)
        self.conn.commit()
        return res

    def delete(self,student_id):
        sql = "DELETE FROM student_info WHERE id=%s;"
        res = self.cursor.execute(sql,student_id)
        self.conn.commit()
        return res

    #获取最大学生id
    def get_student_id(self):
        sql = "SELECT MAX(id) FROM student_info;"
        res = self.cursor.execute(sql)
        # print(self.cursor.fetchone())
        current_id = self.cursor.fetchone()
        if current_id:
            current_id = current_id[0]
        else:
            current_id = 1
        return current_id

    def __del__(self):
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    mh = mysqlHandler()
    # mh.write([2,"alex","123","female",16])
    # print(mh.delete(2))
    # print(mh.read())
    print(mh.get_student_id())