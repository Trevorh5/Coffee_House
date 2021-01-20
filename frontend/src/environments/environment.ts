export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000', // the running FLASK api server url
  auth0: {
    url: 'coffee-shop-udemy.us', // the auth0 domain prefix
    audience: 'https://coffee-shop-api/', // the audience set for the auth0 app
    clientId: 'JVwinuBQp5yd40HPqZm97Ztr3aDo8F3s', // the client id generated for the auth0 app
    callbackURL: 'http://localhost:8100', // the base url of the running ionic application. 
  }
};
