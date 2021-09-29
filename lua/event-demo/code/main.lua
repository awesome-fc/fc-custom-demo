local ngx = require('ngx')
local json = require('json')

local path = ngx.var.request_uri
local body = ngx.req.get_body_data()
local headers = ngx.req.get_headers()
local rid = headers["x-fc-request-id"]
if body == nil then
   body = ""
end

if path == '/initialize' then
   print("FC Initialize Start RequestId: ", rid)
   -- local event = json.decode(body)
   -- do your logic ...
   print("init")
   ngx.say(body)
   print("FC Initialize End RequestId: ", rid)
   ngx.exit(0)
end

if path == '/invoke' then
   print("FC Invoke Start RequestId: ", rid)
   -- local event = json.decode(body)
   -- do your logic ...
   print(body)
   ngx.say(body)
   print("FC Invoke End RequestId: ", rid)
   ngx.exit(0)
end

local resp = {}
resp['errorMessage'] = 'unsupported event: ' .. body
ngx.say(json.encode(resp))
ngx.exit(0)
