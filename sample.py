import sqlite3
from flask import jsonify, request
from flask_restful import Resource

room_list = []

def db_connection():
    conn = None
    try:
        conn = sqlite3.Connection('RoomManagement.sqlite')
    except sqlite3.Error as e:
        print(e)
    return conn

def createdb():
    conn = sqlite3.connect('RoomManagement.sqlite')
    cursor = conn.cursor()
    sql_query = """CREATE TABLE IF NOT EXISTS Room (
        roomId integer PRIMARY KEY,
        scannerId integer NOT NULL,
        name text NOT NULL,
        min integer NOT NULL,
        max integer NOT NULL
    )"""

    cursor.execute(sql_query)
    return "DB Created"




# Handle Room Management
# class RoomResource(Resource):
#
#     def get(self):
#         createdb()
#         conn = db_connection()
#         cursor = conn.cursor()
#         cursor = conn.execute('SELECT * FROM Room')
#         room_list = [
#             dict(roomId=row[0], scannerId=row[1], name=row[2], min=row[3], max=row[4])
#             for row in cursor.fetchall()
#         ]
#         if len(room_list) > 0:
#             return jsonify(room_list)
#         else:
#             return 'Not Found', 404
#
#     def post(self):
#         conn = db_connection()
#         cursor = conn.cursor()
#         content = request.json
#
#         new_roomId = int(content['RoomID'])
#         new_scannerId = int(content['ScannerID'])
#         new_name = content['Name']
#         new_min = int(content['Min'])
#         new_max = int(content['Max'])
#
#         sql_query = """INSERT INTO Room (roomId, scannerId, name, min, max) values (?,?,?,?,?)"""
#         try:
#             cur = cursor.execute(sql_query, (new_roomId, new_scannerId, new_name, new_min, new_max))
#             conn.commit()
#         except sqlite3.Error as e:
#             print(e)
#         finally:
#             conn.close()
#         return jsonify('added ', 201)

# class RoomUpdateResource(Resource):
#
#     def get(self, roomId):
#         createdb()
#         conn = db_connection()
#         cursor = conn.cursor()
#         cursor.execute("select * from Room where roomId = ?", (roomId,))
#         rows = cursor.fetchall()
#         for r in rows:
#             room = r
#             if room is not None:
#                 return jsonify(room)
#         return jsonify('something wrong', 404)

    # def put(self, roomId):
    #     conn = db_connection()
    #     cursor = conn.cursor()
    #     content = request.json
    #
    #     new_scannerId = int(content['ScannerID'])
    #     new_name = content['Name']
    #     new_min = int(content['Min'])
    #     new_max = int(content['Max'])

        # updated_room = {
        #     "roomId": roomId,
        #     "scannerId": new_scannerId,
        #     "name": new_name,
        #     "min": new_min,
        #     "max": new_max
        # }
        # sql_query = """update Room set scannerId=?,name=?, min=?, max=? WHERE roomId =? """
        # try:
        #     conn.execute(sql_query, (new_scannerId, new_name, new_min, new_max, roomId))
        #     conn.commit()
        # except sqlite3.Error as e:
        #     print(e)
        # finally:
        #     conn.close()
        # return jsonify(updated_room, 201)

    # def delete(self, roomId):
    #     conn = db_connection()
    #     cursor = conn.cursor()
    #     sql_query = """DELETE FROM Room where roomId=?"""
    #     try:
    #         conn.execute(sql_query, (roomId,))
    #         conn.commit()
    #     except sqlite3.Error as e:
    #         print(e)
    #     finally:
    #         conn.close()
    #     return jsonify('deleted ', 201)