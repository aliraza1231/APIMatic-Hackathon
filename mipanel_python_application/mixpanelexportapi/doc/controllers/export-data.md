# Export Data

```python
export_data_controller = client.export_data
```

## Class Name

`ExportDataController`


# Mixpanel-Events-Data

Get Mixpanel Events

```python
def mixpanel_events_data(self,
                        from_date,
                        to_date,
                        where,
                        project_id,
                        accept,
                        limit=None,
                        event=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `from_date` | `string` | Query, Required | The date in yyyy-mm-dd format to begin querying from. This date is inclusive. |
| `to_date` | `string` | Query, Required | The date in yyyy-mm-dd format to query to. This date is inclusive. |
| `where` | `string` | Query, Required | An expression to filter events by. |
| `project_id` | `int` | Query, Required | Your Mixpanel Project Id. |
| `accept` | `string` | Header, Required | - |
| `limit` | `int` | Query, Optional | The max number of events to be returned. |
| `event` | `List of string` | Query, Optional | The event or events that you wish to get data for, encoded as a JSON array. |

## Response Type

`string`

## Example Usage

```python
from_date = '2022-05-28'
to_date = '2022-05-28'
where = 'defined(properties["$username"])'
project_id = 690335
accept = 'text/plain'
limit = 10
event = ['SignUp']

result = export_data_controller.mixpanel_events_data(from_date, to_date, where, project_id, accept, limit, event)
```

## Example Response

```
"{\"event\":\"SignUp\",\"properties\":{\"time\":1653780151,\"distinct_id\":\"629205cc781766d578818412\",\"$insert_id\":\"edc12225-2403-5bee-af50-3c677bab8870\",\"$mp_api_endpoint\":\"api.mixpanel.com\",\"$mp_api_timestamp_ms\":1653736953690,\"$referrer\":\"SearchEngine\",\"$username\":\"anushka.icapotech@gmail.com\",\"AnonymousId\":\"fwgjn5euppxzmdrqp3xa1qzw\",\"ApiChallenges\":[\"Api Documentation\"],\"Company\":\"Icapotech\",\"CreationDate\":\"2022-05-28T23:21:48\",\"Email\":\"anushka.icapotech@gmail.com\",\"Industry\":\"Energy\",\"JobFunction\":\"Product/Project Management\",\"Name\":\"Anushka Sinha\",\"PhoneNumber\":\"91-9137557305\",\"PlanName\":\"trial-it4\",\"RegisterFlow\":\"transformer\",\"SignUpType\":\"Regular\",\"id\":\"629205cc781766d578818412\",\"mp_lib\":\"Segment: Analytics.NET\",\"mp_processing_time_ms\":1653736953733}}\n{\"event\":\"TransformViaWeb\",\"properties\":{\"time\":1653781169,\"distinct_id\":\"629205cc781766d578818412\",\"$insert_id\":\"55cf842d-dde1-5fce-8e51-5d30a47e9e05\",\"$mp_api_endpoint\":\"api.mixpanel.com\",\"$mp_api_timestamp_ms\":1653737971651,\"$username\":\"anushka.icapotech@gmail.com\",\"APIDescription\":\"https://apimatic.io/apientity/export/YXBpbWF0aWNf\",\"APIName\":\"AC Operation\",\"ApimaticVersion\":\"V3.0\",\"AuthType\":\"None\",\"BaseURI\":\"Server 1\",\"Endpoints\":1,\"ExportFormat\":\"Postman20\",\"FileName\":\"AC Operation.postman_collection.json\",\"FilePath\":\"https://apimatic.io/api/transformations/629209ef781766d5788187aa/input-file\",\"FileUrl\":\"\",\"ImportFormat\":\"Postman2\",\"ImportScheme\":\"Single\",\"Models\":2,\"TestCases\":1,\"TransformationEndpoint\":\"TransformationsApiController\",\"UserAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36\",\"email\":\"anushka.icapotech@gmail.com\",\"id\":\"629205cc781766d578818412\",\"mp_lib\":\"Segment: Analytics.NET\",\"mp_processing_time_ms\":1653737971710,\"url\":\"https://apimatic.io/apientity/#!//edit\"}}\n{\"event\":\"TransformViaWeb\",\"properties\":{\"time\":1653781226,\"distinct_id\":\"629205cc781766d578818412\",\"$insert_id\":\"b92acbac-3e78-56cc-bb26-de1844e8e7b0\",\"$mp_api_endpoint\":\"api.mixpanel.com\",\"$mp_api_timestamp_ms\":1653738028409,\"$username\":\"anushka.icapotech@gmail.com\",\"APIDescription\":\"https://apimatic.io/apientity/export/YXBpbWF0aWNf\",\"APIName\":\"AC Operation\",\"ApimaticVersion\":\"V3.0\",\"AuthType\":\"None\",\"BaseURI\":\"Server 1\",\"Endpoints\":1,\"ExportFormat\":\"Swagger20\",\"FileName\":\"AC Operation.postman_collection.json\",\"FilePath\":\"https://apimatic.io/api/transformations/62920a2a781766d5788187f2/input-file\",\"FileUrl\":\"\",\"ImportFormat\":\"Postman2\",\"ImportScheme\":\"Single\",\"Models\":2,\"TestCases\":1,\"TransformationEndpoint\":\"TransformationsApiController\",\"UserAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36\",\"email\":\"anushka.icapotech@gmail.com\",\"id\":\"629205cc781766d578818412\",\"mp_lib\":\"Segment: Analytics.NET\",\"mp_processing_time_ms\":1653738028449,\"url\":\"https://apimatic.io/apientity/#!//edit\"}}\n{\"event\":\"SignUp\",\"properties\":{\"time\":1653721152,\"distinct_id\":\"62911f1f781766d578733e3e\",\"$insert_id\":\"aae89509-68fd-56d0-b03c-8cf6567e6688\",\"$mp_api_endpoint\":\"api.mixpanel.com\",\"$mp_api_timestamp_ms\":1653677954894,\"$referrer\":\"SearchEngine\",\"$username\":\"amorales@baufest.com\",\"AnonymousId\":\"j0oikn5og154rciiuhqi0m2l\",\"ApiChallenges\":[\"Interactive Explorer\"],\"Company\":\"Baufest\",\"CreationDate\":\"2022-05-28T06:57:35\",\"Email\":\"amorales@baufest.com\",\"Industry\":\"Blockchain Solutions\",\"JobFunction\":\"Engineering\",\"Name\":\"Alexis Vega\",\"PhoneNumber\":\"52-5612939425\",\"PlanName\":\"trial-it4\",\"RegisterFlow\":\"Account/Login\",\"SignUpType\":\"Regular\",\"id\":\"62911f1f781766d578733e3e\",\"mp_lib\":\"Segment: Analytics.NET\",\"mp_processing_time_ms\":1653677954958}}\n{\"event\":\"Import_Failed\",\"properties\":{\"time\":1653721259,\"distinct_id\":\"62911f1f781766d578733e3e\",\"$insert_id\":\"320ed8cb-c8ba-54eb-937b-ed0f2947fa58\",\"$mp_api_endpoint\":\"api.mixpanel.com\",\"$mp_api_timestamp_ms\":1653678062268,\"$username\":\"amorales@baufest.com\",\"ApimaticVersion\":\"V3.0\",\"FailureMessage\":\"We could not identify the API description format from the given file. Please ensure your file is in one of the following supported formats: <i><code>OpenAPI/Swagger</code></i>, <i><code>RAML</code></i>, <i><code>API Blueprint</code></i>, <i><code>WADL</co\",\"FilePath\":\"https://apimaticio.blob.core.windows.net/api-descriptions/Imported Api/9a2d8eaa-09b0-4782-bf89-98373a95c6d6\",\"ImportFormat\":\"Unknown\",\"ImportScheme\":\"Single\",\"ImportType\":\"FileUpload_Website\",\"email\":\"amorales@baufest.com\",\"id\":\"62911f1f781766d578733e3e\",\"mp_lib\":\"Segment: Analytics.NET\",\"mp_processing_time_ms\":1653678062326}}\n{\"event\":\"ImportAPI\",\"properties\":{\"time\":1653721385,\"distinct_id\":\"62911f1f781766d578733e3e\",\"$insert_id\":\"7de115a1-8cee-5eb0-8118-a8487da1d60a\",\"$mp_api_endpoint\":\"api.mixpanel.com\",\"$mp_api_timestamp_ms\":1653678187308,\"$username\":\"amorales@baufest.com\",\"APIDescription\":\"https://apimatic.io/apientity/export/YXBpbWF0aWNfNjI5MTIwNjg3ODE3NjZkNTc4NzM0NTgw\",\"APIName\":\"aple-apislending/gateway\",\"API_ID\":\"62912068781766d578734580\",\"ApimaticVersion\":\"V3.0\",\"AuthType\":\"None\",\"BaseURI\":\"default\",\"Endpoints\":7,\"FilePath\":\"https://apimaticio.blob.core.windows.net/api-descriptions/Imported Api/d5989407-fa6b-4c4c-ba72-4d6e464b301d\",\"ImportFormat\":\"OpenApi3Json\",\"ImportScheme\":\"Single\",\"Models\":17,\"TestCases\":0,\"email\":\"amorales@baufest.com\",\"id\":\"62911f1f781766d578733e3e\",\"mp_lib\":\"Segment: Analytics.NET\",\"mp_processing_time_ms\":1653678187365,\"url\":\"https://apimatic.io/apientity/#!/62912068781766d578734580/edit\"}}\n{\"event\":\"ApiOpenedInApiEditor\",\"properties\":{\"time\":1653721399,\"distinct_id\":\"62911f1f781766d578733e3e\",\"$insert_id\":\"f345e48b-f648-5a2f-bf5a-188b3f2a959b\",\"$mp_api_endpoint\":\"api.mixpanel.com\",\"$mp_api_timestamp_ms\":1653678201679,\"$referrer\":\"dashboard\",\"$username\":\"amorales@baufest.com\",\"ApimaticVersion\":\"V3.0\",\"CurrentUrl\":\"apientity/edit/62912068781766d578734580\",\"email\":\"amorales@baufest.com\",\"id\":\"62911f1f781766d578733e3e\",\"mp_lib\":\"Segment: Analytics.NET\",\"mp_processing_time_ms\":1653678201709}}\n{\"event\":\"SDKGenerated_WEBSITE\",\"properties\":{\"time\":1653721453,\"distinct_id\":\"62911f1f781766d578733e3e\",\"$insert_id\":\"56d41b4f-9332-561b-9ada-732081246b0d\",\"$mp_api_endpoint\":\"api.mixpanel.com\",\"$mp_api_timestamp_ms\":1653678255405,\"$username\":\"amorales@baufest.com\",\"APIDescription\":\"https://apimatic.io/apientity/export/YXBpbWF0aWNfNjI5MTIwNjg3ODE3NjZkNTc4NzM0NTgw\",\"APIName\":\"aple-apislending/gateway\",\"API_ID\":\"62912068781766d578734580\",\"ApimaticVersion\":\"V3.0\",\"AuthType\":\"None\",\"BaseURI\":\"default\",\"Endpoints\":7,\"FromCache\":false,\"GeneratedFilePath\":\"https://www.apimatic.iohttps://www.apimatic.io/api/api-entities/62912068781766d578734580/code-generations/629120ac781766d578734cfd/generated-sdk\",\"Language\":\"CS_NET_STANDARD_LIB\",\"Models\":17,\"OwnerEmail\":\"amorales@baufest.com\",\"TestCases\":0,\"UserAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39\",\"email\":\"amorales@baufest.com\",\"id\":\"62911f1f781766d578733e3e\",\"mp_lib\":\"Segment: Analytics.NET\",\"mp_processing_time_ms\":1653678255571,\"url\":\"https://apimatic.io/apientity/#!/62912068781766d578734580/edit\"}}\n{\"event\":\"Export_APIDescription\",\"properties\":{\"time\":1653721490,\"distinct_id\":\"62911f1f781766d578733e3e\",\"$insert_id\":\"8ff50879-a1e4-54ba-8607-d1efe314e7b3\",\"$mp_api_endpoint\":\"api.mixpanel.com\",\"$mp_api_timestamp_ms\":1653678342678,\"$username\":\"amorales@baufest.com\",\"APIDescription\":\"https://apimatic.io/apientity/export/YXBpbWF0aWNfNjI5MTIwNjg3ODE3NjZkNTc4NzM0NTgw\",\"APIName\":\"aple-apislending/gateway\",\"API_ID\":\"62912068781766d578734580\",\"ApimaticVersion\":\"V3.0\",\"AuthType\":\"None\",\"BaseURI\":\"default\",\"Endpoints\":7,\"Format\":\"Swagger20\",\"Models\":17,\"TestCases\":0,\"email\":\"amorales@baufest.com\",\"id\":\"62911f1f781766d578733e3e\",\"mp_lib\":\"Segment: Analytics.NET\",\"mp_processing_time_ms\":1653678342740,\"url\":\"https://apimatic.io/apientity/#!/62912068781766d578734580/edit\"}}\n{\"event\":\"ImportAPI\",\"properties\":{\"time\":1653732099,\"distinct_id\":\"62911f1f781766d578733e3e\",\"$insert_id\":\"ef7ca04c-9608-57d3-b537-97942099da97\",\"$mp_api_endpoint\":\"api.mixpanel.com\",\"$mp_api_timestamp_ms\":1653688901708,\"$username\":\"amorales@baufest.com\",\"APIDescription\":\"https://apimatic.io/apientity/export/YXBpbWF0aWNfNjI5MTRhNDI3ODE3NjZkNTc4N2JjYmQ3\",\"APIName\":\"aple-apislending/gateway\",\"API_ID\":\"62914a42781766d5787bcbd7\",\"ApimaticVersion\":\"V3.0\",\"AuthType\":\"None\",\"BaseURI\":\"default\",\"Endpoints\":7,\"FilePath\":\"https://apimaticio.blob.core.windows.net/api-descriptions/Imported Api/9ee97ac6-73fd-44b8-8189-ace599e05aff\",\"ImportFormat\":\"OpenApi3Json\",\"ImportScheme\":\"Single\",\"Models\":17,\"TestCases\":0,\"email\":\"amorales@baufest.com\",\"id\":\"62911f1f781766d578733e3e\",\"mp_lib\":\"Segment: Analytics.NET\",\"mp_processing_time_ms\":1653688901763,\"url\":\"https://apimatic.io/apientity/#!/62914a42781766d5787bcbd7/edit\"}}\n"
```

