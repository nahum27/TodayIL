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



#### *. Have your application request authorization*

The request is sent to the `/api/token` endpoint of the Accounts service:

```
POST https://accounts.spotify.com/api/token
```

The body of this POST request must contain the following parameters encoded in `application/x-www-form-urlencoded` as defined in the OAuth 2.0 specification:

| REQUEST BODY PARAMETER | VALUE                                       |
| :--------------------- | :------------------------------------------ |
| grant_type             | *Required.* Set it to `client_credentials`. |

The header of this POST request must contain the following parameter:

| HEADER PARAMETER | VALUE                                                        |
| :--------------- | :----------------------------------------------------------- |
| Authorization    | *Required.* Base 64 encoded string that contains the client ID and client secret key. The field must have the format: Authorization: `Basic `  <base64 encoded client_id:client_secret> |



## Response Status Codes

Web API uses the following response status codes, as defined in the [RFC 2616](https://www.ietf.org/rfc/rfc2616.txt) and [RFC 6585](https://www.ietf.org/rfc/rfc6585.txt):

| STATUS CODE | DESCRIPTION                                                  |
| :---------- | :----------------------------------------------------------- |
| 200         | OK - The request has succeeded. The client can read the result of the request in the body and the headers of the response. |
| 201         | Created - The request has been fulfilled and resulted in a new resource being created. |
| 202         | Accepted - The request has been accepted for processing, but the processing has not been completed. |
| 204         | No Content - The request has succeeded but returns no message body. |
| 304         | Not Modified. See [Conditional requests](https://developer.spotify.com/documentation/web-api/#conditional-requests). |
| 400         | Bad Request - The request could not be understood by the server due to malformed syntax. The message body will contain more information; see [Response Schema](https://developer.spotify.com/documentation/web-api/#response-schema). |
| 401         | Unauthorized - The request requires user authentication or, if the request included authorization credentials, authorization has been refused for those credentials. |
| 403         | Forbidden - The server understood the request, but is refusing to fulfill it. |
| 404         | Not Found - The requested resource could not be found. This error can be due to a temporary or permanent condition. |
| 429         | Too Many Requests - [Rate limiting](https://developer.spotify.com/documentation/web-api/#rate-limiting) has been applied. |
| 500         | Internal Server Error. You should never receive this error because our clever coders catch them all … but if you are unlucky enough to get one, please report it to us through a comment at the bottom of this page. |
| 502         | Bad Gateway - The server was acting as a gateway or proxy and received an invalid response from the upstream server. |
| 503         | Service Unavailable - The server is currently unable to handle the request due to a temporary condition which will be alleviated after some delay. You can choose to resend the request again. |



## Rate Limiting

Rate Limiting enables Web API to share access bandwidth to its resources equally across all users.

Rate limiting is applied as per application based on Client ID, and regardless of the number of users who use the application simultaneously.

To reduce the amount of requests, use endpoints that fetch multiple entities in one request. For example: If you often request single tracks, albums, or artists, use endpoints such as [Get Several Tracks](https://developer.spotify.com/documentation/web-api/reference/tracks/get-several-tracks/), [Get Several Albums](https://developer.spotify.com/documentation/web-api/reference/albums/get-several-albums/) or [Get Several Artists](https://developer.spotify.com/documentation/web-api/reference/artists/get-several-artists/), instead.

**Note:** If Web API returns **status code 429**, it means that you have sent too many requests. When this happens, check the `Retry-After` header, where you will see a number display





![data_pipeline](https://user-images.githubusercontent.com/30791788/81191861-7838c500-8ff4-11ea-96ff-a4b6145c4d98.png)



##### Reponse Info

Web Api : https://developer.spotify.com/documentation/web-api/reference/artists/get-artist/

### artist object (full)

 

| KEY           | VALUE TYPE                                                   | VALUE DESCRIPTION                                            |
| :------------ | :----------------------------------------------------------- | :----------------------------------------------------------- |
| external_urls | an [external URL object](https://developer.spotify.com/documentation/web-api/reference/object-model/#external-url-object) | Known external URLs for this artist.                         |
| followers     | A [followers object](https://developer.spotify.com/documentation/web-api/reference/object-model/#followers-object) | Information about the followers of the artist.               |
| genres        | array of strings                                             | A list of the genres the artist is associated with. For example: `"Prog Rock"` , `"Post-Grunge"`. (If not yet classified, the array is empty.) |
| href          | string                                                       | A link to the Web API endpoint providing full details of the artist. |
| id            | string                                                       | The [Spotify ID](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the artist. |
| images        | array of [image objects](https://developer.spotify.com/documentation/web-api/reference/object-model/#image-object) | Images of the artist in various sizes, widest first.         |
| name          | string                                                       | The name of the artist                                       |
| popularity    | int                                                          | The popularity of the artist. The value will be between 0 and 100, with 100 being the most popular. The artist’s popularity is calculated from the popularity of all the artist’s tracks. |
| type          | string                                                       | The object type: `"artist"`                                  |
| uri           | string                                                       | The [Spotify URI](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the artist. |

```curl-command
curl -X GET "https://api.spotify.com/v1/artists/0OdUWJ0sBjDrqHygGUXeCF" -H 
"Authorization: Bearer {your access token}"

{
  "external_urls" : {
    "spotify" : "https://open.spotify.com/artist/0OdUWJ0sBjDrqHygGUXeCF"
  },
  "followers" : {
    "href" : null,
    "total" : 306565
  },
  "genres" : [ "indie folk", "indie pop" ],
  "href" : "https://api.spotify.com/v1/artists/0OdUWJ0sBjDrqHygGUXeCF",
  "id" : "0OdUWJ0sBjDrqHygGUXeCF",
  "images" : [ {
    "height" : 816,
    "url" : "https://i.scdn.co/image/eb266625dab075341e8c4378a177a27370f91903",
    "width" : 1000
  }, {
    "height" : 522,
    "url" : "https://i.scdn.co/image/2f91c3cace3c5a6a48f3d0e2fd21364d4911b332",
    "width" : 640
  }, {
    "height" : 163,
    "url" : "https://i.scdn.co/image/2efc93d7ee88435116093274980f04ebceb7b527",
    "width" : 200
  }, {
    "height" : 52,
    "url" : "https://i.scdn.co/image/4f25297750dfa4051195c36809a9049f6b841a23",
    "width" : 64
  } ],
  "name" : "Band of Horses",
  "popularity" : 59,
  "type" : "artist",
  "uri" : "spotify:artist:0OdUWJ0sBjDrqHygGUXeCF"
}
```

![spotifyentity](https://user-images.githubusercontent.com/30791788/81193331-3872dd00-8ff6-11ea-975e-a66ca0022d00.png)











04





















