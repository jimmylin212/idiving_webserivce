# idiving_webserivce
The back-end web service for iDiving

## 使用方式

Base URL: 

### 會員資料
URL: `https//<BASE_URL>/_ah/api/internal/v1/member`

Accept Method: POST, PUT, PATCH

Accept Columns: Please check the class MemberRequest within [messages](https://github.com/jimmylin212/idiving_webserivce/blob/master/models/messages.py).py

#### 查詢
Method: POST
Example: 
```
{
    "id_number": "A123456789",
}
```

#### 新增
Method: PUT
Example:
```
{
    "id_number": "A123456789",
    "aa_deposit": true
}
```

#### 修改
Method: PATCH
Example:
```
{
    "id_number" : "F123456780",
    "height" : 178
}
```
