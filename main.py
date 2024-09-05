from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth
import boto3

from fastapi import FastAPI

app = FastAPI()

@app.get("/opensearch")
def read_root():
    
    response = client.search(
        body = query,
        index = 'opensearch_dashboards_sample_data_flights'
    )

    print('response - match xico')
    print(response)
    
    return {"Hello": "World"}

host = 'vpc-yr-vtr-kk66ndzelsd5nyucwx7h2dvkoi.ap-northeast-2.es.amazonaws.com' # cluster endpoint, for example: my-test-domain.us-east-1.es.amazonaws.com
region = 'ap-northeast-2'
service = 'es'
credentials = boto3.Session().get_credentials()
auth = AWSV4SignerAuth(credentials, region, service)

client = OpenSearch(
    hosts = [{'host': host, 'port': 443}],
    http_auth = auth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection,
    pool_maxsize = 20
)

q = 'xico'
query = {
  'size': 5,
  'query': {
    'multi_match': {
      'query': q,
      'fields': ['FlightNum', 'OriginCityName', 'DestCityName']
    }
  }
}
