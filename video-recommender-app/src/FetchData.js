/**
 * fetch data from web api using flask_app
 * @param {string} relUrl relative url of route
 * @returns response
 */
 async function FetchData(relUrl) {
  return fetch('http://127.0.0.1:5000/' + relUrl, {
    method: 'GET'
  }).then((res) => res.json());
}

export default FetchData;
