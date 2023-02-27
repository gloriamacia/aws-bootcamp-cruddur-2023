# Week 2 — Distributed Tracing


## HoneyComb

When creating a new dataset in Honeycomb it will provide all these installation [instructions](https://docs.honeycomb.io/getting-data-in/opentelemetry/python/) 

You'll need to grab the API key from your honeycomb account:

```sh
export HONEYCOMB_API_KEY=""
export HONEYCOMB_SERVICE_NAME="Cruddur"
gp env HONEYCOMB_API_KEY=""
gp env HONEYCOMB_SERVICE_NAME="Cruddur"
```

We'll add the following files to our `requirements.txt`

```
opentelemetry-api 
opentelemetry-sdk 
opentelemetry-exporter-otlp-proto-http 
opentelemetry-instrumentation-flask 
opentelemetry-instrumentation-requests
```

We'll install these dependencies:

```sh
pip install -r requirements.txt
```

Add to the `app.py`

```py
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
```

```py
# Initialize tracing and an exporter that can send data to Honeycomb
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)
```

```py
# Initialize automatic instrumentation with Flask
app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()
```

Add teh following Env Vars to `backend-flask` in docker compose

```yml
OTEL_EXPORTER_OTLP_ENDPOINT: "https://api.honeycomb.io"
OTEL_EXPORTER_OTLP_HEADERS: "x-honeycomb-team=${HONEYCOMB_API_KEY}"
OTEL_SERVICE_NAME: "${HONEYCOMB_SERVICE_NAME}"
```
When it works you will see something like this: 

<img width="70%" alt="Screenshot 2023-02-27 at 22 21 48" src="https://user-images.githubusercontent.com/17580456/221711098-d62c4439-f30a-4c53-b603-6c2148f79cdb.png">

We can run custom queries and by clicking on the pen icon, save them for later (homework as well) 

<img width="70%" alt="Screenshot 2023-02-27 at 23 58 01" src="https://user-images.githubusercontent.com/17580456/221711155-9a36210a-d133-4283-b22d-f6893eab4956.png">

We can create [spans](https://docs.honeycomb.io/getting-data-in/opentelemetry/python/)

We see two colors: 

<img width="70%" alt="Screenshot 2023-02-27 at 23 55 11" src="https://user-images.githubusercontent.com/17580456/221711121-eda9933b-6f5a-4fd4-b5da-f47a17ab98d1.png">

<img width="70%" alt="Screenshot 2023-02-27 at 23 56 03" src="https://user-images.githubusercontent.com/17580456/221711138-ef7ea93c-cfc4-4d6b-8f73-237e3d7e9d0b.png">

As part of my homework, I added a custom span that returns the ID of the post most liked:

```py
likes = []
for e in results:
  likes.append(e['likes'])
max_idx = likes.index(max(likes))
span.set_attribute("app.max.likes.id", results[max_idx]['uuid'])
```

<img width="70%" alt="Screenshot 2023-02-28 at 00 09 42" src="https://user-images.githubusercontent.com/17580456/221711175-08327cb3-c714-44ad-bfd2-efca04b7532d.png">



