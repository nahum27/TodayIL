## SPOTIFY WEB API

> URL : https://developer.spotify.com/documentation/web-api/
>
> Authorization Guide : https://developer.spotify.com/documentation/general/guides/authorization-guide/
>
> DashBoard : https://developer.spotify.com/dashboard/



> SPOTIFY는 국내에 정식 서비스를 하지 않아 다른 가입에 VPN을 사용하여 가입한다.
>
> VPN Free - Betternet Unlimited VPN Proxy
>
> https://chrome.google.com/webstore/detail/vpn-free-betternet-unlimi/gjknjjomckknofjidppipffbpoekiipm



- 대시 보드 생성 -> ID, Secret 취득
  -  Data_engineering
    - Client ID
    - Client Secret



#### Authorization Guide for use web api

**Client Credentials Flow**

> The Client Credentials flow is used in **server-to-server** authentication. Only endpoints that do not access user information can be accessed. The advantage here in comparison with requests to the Web API made without an access token, is that a higher rate limit is applied.

| **You do**  | Login with your **Client ID** and **Secret Key**. |
| ----------- | ------------------------------------------------- |
| **You get** | **Access token**.                                 |

![Spotify_client_CredentialsFlows](https://user-images.githubusercontent.com/30791788/81048848-09764180-8ef8-11ea-9d6a-87ff9447da24.png)



- Spotify api 에게 토큰 발행

`