#!/usr/bin/env python3
"""
Write a Python script that provides some stats about Nginx logs stored in MongoDB:
"""
from pymongo import MongoClient


if __name__ == "__main__":
    data = MongoClient().logs.nginx
    print(f'{data.count_documents({})} logs\nMethods:')
    print(f'\tmethod GET: {data.count_documents({"method": "GET"})}')
    print(f'\tmethod POST: {data.count_documents({"method": "POST"})}')
    print(f'\tmethod PUT: {data.count_documents({"method": "PUT"})}')
    print(f'\tmethod PATCH: {data.count_documents({"method": "PATCH"})}')
    print(f'\tmethod DELETE: {data.count_documents({"method": "DELETE"})}')
    print(f'{data.count_documents({"path": "/status"})} status check')
