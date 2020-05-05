### API(Application Programming Interface)

- 두개의 시스템이 서로 상호 작용하기 위한 인터페이스 
  - 데이터를 주고 받는 인터페이스
  - API라 하면 보통 REST API를 지칭



### API 접근 권한

> Authentcation VS Authorization

- Authentication : identity(정체)가 맞다는 증명
- Authorization : API를 통한 어떠한 액션을 허용

API가 Authentication을 하여도 어떠한 액션에 대해서는 Authorization을 허용하지 않을 수 있음



#### Basic Auth

> Basic Auth의 경우 username:password와 같은 Creadential을 Base64로 인코딩한 값을 Request Header d안에 포함

|Authorization  Basic|

```python
encode = base64.b64encode("{}:{}".format(self.client_id, self.client_secret))
base_url = "https://accounts.spotify.com/api/token"
headers = {"Authorization": "Basic {}".format(encoded)}
```



#### OAuth 2.0

> OAuth는 서버와 클라이언트 사이에 인증을 완료하면 서버는 권한부여의 결과로써 `access token`을 전송합니다. 클라이언트는 access token을 이용해서 접근 및 서비스를 요청할 수 있습니다. 서버는 access token 기반으로 서비스와 권한을 확인하여 접근을 허용할지 말지를 결정하고, 결과 데이터를 클라이언트에게 보내줍니다. 서버는 access token을 기반으로 클라이언트를 확인하여 서비스하기 때문에, 세션([`session`](https://en.wikipedia.org/wiki/Session_(computer_science)))이나 쿠키([`cookie`](https://en.wikipedia.org/wiki/HTTP_cookie)를 이용해 클라이언트의 상태정보를 유지할 필요가 없습니다.



> OAuth 2.0은 외부 서비스(third-party application)의 인증 및 권한부여를 관리하는 범용 [프레임워크](https://en.wikipedia.org/wiki/Software_framework) 입니다. OAuth 기반 서비스의 API를 호출을 할 때에는, [HTTP 헤더](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)에 access token을 포함하여 요청을 보내게 됩니다. 서비스는 access token을 검사하면서 이 요청이 유효한지 판단하여 적절한 결과를 응답합니다.
>
> 사용자 입장에선 OAuth의 권한 요청 절차는 access token을 획득하는 것이 가장 주요한 목적이라 할 수 있고, 서비스 제공자 입장에선 인증된 사용자(!)에게 access token을 발급하는 것이 가장 중요한 일이라 할 수 있습니다.

##### OAuth를 구성하고 있는 주요 4가지 객체(Roles)

- `resource owner`(자원 소유자)는 `protected resource`(보호된 자원)에 접근하는 권한을 제공합니다.
- `resource server`(자원 서버)는 access token을 사용해서 요청(request)을 수신할 때, 권한을 검증한 후 적절한 결과를 응답합니다.
- `client`(클라이언트)는 `resource owner`(자원 소유자)의 `protected resource`(보호된 자원)에 접근을 요청을 하는 애플리케이션(application)입니다.
- `authorization Server`(권한 서버)는 `client`(클라이언트)가 성공적으로 access token을 발급받은 이후에 `resource owner`(자원 소유자)를 인증하고 `obtaining authorization`(권한 부여)를 합니다.

![OAuth](https://user-images.githubusercontent.com/30791788/81042331-dbd6cb80-8eea-11ea-9ec9-b04b13437615.png)