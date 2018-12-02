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
### Authorize

* authorize via python will automagically hit the redirect if I query from [Advanced Rest Client](https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo?hl=en-US)
with the response_type as `token` and response_mode as `fragment`
* authorize via python will return an HTML