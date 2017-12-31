# idiving_webserivce
The back-end web service for iDiving

## Usage

Base URL: 

### Member Data
URL: `https://<BASE_URL>/_ah/api/internal/v1/member`

Accept Method: POST, PUT, PATCH

Accept Columns: Please check the class [MemberRequest](https://github.com/jimmylin212/idiving_webserivce/blob/master/models/messages.py#L6) within messages.py file.

#### Search member
Method: POST
Example: 
```
{
    "id_number": "A123456789",
}
```

#### Add new member
Method: PUT
Example:
```
{
    "id_number": "A123456789",
    "aa_deposit": true
}
```

#### Update member data
Method: PATCH
Example:
```
{
    "id_number" : "F123456780",
    "height" : 178
}
```
