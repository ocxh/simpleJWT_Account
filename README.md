# simpleJWT_Account
- djangoresftframework
- simpleJWT
- token(refresh/access)
- custom UserModel

## APIS
|path|description|request|response|
|------|---|---|---|
|/token/refresh/|refresh access token|"refresh"|"access"|
|/token/|check access token|"token"|void OR [Expiration msg]|
|/register/|signup|"nickname", "email", "password", "password2"|[Result msg]|
|/login/|signin|"email", "password"| Token(refresh, access)|

<br>

**[Expiration msg]**<br>
~~~
{
    "detail": "Token is invalid or expired",
    "code": "token_not_valid"
}
~~~

**[Result msg]**<br>

~~~
{
    "account": {
        "nickname": "test002",
        "email": "test002@test.com"
    },
    "message": "register successs"
}
~~~

## Custom UserModel
- AbstractBaseUser, PermissionsMixin
- Email, Nickname, Password
