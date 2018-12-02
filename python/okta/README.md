# Okta App

This app is for me to get a better understanding of SAML with Okta on the backend with Python. Currently
Okta does not provide direct integration library to Python so you're left to integrate through the REST
api.

## Okta Workspace Details

* Identity Provider: [https://dev-967684.oktapreview.com/](https://dev-967684.oktapreview.com/)
* Client Id: 0oahwams3hEA80YM40h7


## Notes

* [Choosing a Authentication Flow](https://developer.okta.com/authentication-guide/auth-overview/#choosing-an-oauth-20-flow)
* [Simple React App](https://medium.com/@to_pe/how-to-add-react-to-a-simple-html-file-a11511c0235f)

### Rabbit Hole

It's important to ensure you are getting the correct keys to verify your token. If you `authorize`
against. If you don't setup the correct `baseurl` from the beginning you'll end up chasing your tail.

**Single Sign-on to Okta vs. Okta as the Identity Platform for your API**

```
1. Single sign-on to Okta
This is for the use case where your users are all part of your Okta organization and you would just like to offer them single sign-on with an ID token. In this case Okta is your authorization server, which we refer to as the “Okta Org Authorization Server” and your full URL looks like this:

https://dev-967684.oktapreview.com/oauth2/v1/authorize

2. Okta as the identity platform for your app or API
This is for use cases where Okta is the identity and authorization platform for your application or API, so your users will be logging in to something other than Okta. In this case you are using a Custom Authorization Server inside Okta, and your full URL looks like this:

https://dev-967684.oktapreview.com/oauth2/${authServerId}/v1/authorize

If you have a developer account, you can use the default authorization server that was created along with your account, in which case the full URL looks like this:

https://dev-967684.oktapreview.com/oauth2/default/v1/authorize
```

If you get your `jwks_uri` from an `authServerId` yet your token is coming from single sign-on you'll end up banging your head
on the key board for hours

### Authorize

* authorize via python will automagically hit the redirect if I query from [Advanced Rest Client](https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo?hl=en-US)
with the response_type as `token` and response_mode as `fragment`
* authorize via python will return an HTML