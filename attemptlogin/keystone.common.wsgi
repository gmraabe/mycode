2017-07-30 17:20:20.455 3279 INFO keystone.common.wsgi [req-b28d7cf9-8591-4629-99a1-bdcd85b046b4 - - - - -] POST http://controller:5000/v3/auth/tokens
2017-07-30 17:20:20.506 3279 WARNING keystone.common.wsgi [req-b28d7cf9-8591-4629-99a1-bdcd85b046b4 - - - - -] Authorization failed. The request you have made requires authentication. from 172.16.1.5
2017-07-30 17:20:22.553 3280 INFO keystone.common.wsgi [req-ef70efb4-0b60-4738-b8ba-204c657aebcc - - - - -] GET http://controller:5000/v3/
2017-07-30 17:20:22.564 3279 INFO keystone.common.wsgi [req-2a491a01-a525-46e6-ba26-b2d53ab02567 - - - - -] POST http://controller:5000/v3/auth/tokens
2017-07-30 17:20:22.727 3279 INFO keystone.token.providers.fernet.utils [req-2a491a01-a525-46e6-ba26-b2d53ab02567 - - - - -] Loaded 2 encryption keys (max_active_keys=3) from: /etc/keystone/fernet-keys/
2017-07-30 17:20:24.228 3280 INFO keystone.common.wsgi [req-e34f17f4-4957-4117-a174-73fb8de19d29 - - - - -] POST http://controller:5000/v3/auth/tokens
2017-07-30 17:20:24.293 3280 WARNING keystone.common.wsgi [req-e34f17f4-4957-4117-a174-73fb8de19d29 - - - - -] Authorization failed. The request you have made requires authentication. from 172.16.1.5
2017-07-30 17:20:29.055 3278 INFO keystone.common.wsgi [req-98982a97-90ca-411f-843d-c4dd5186fe5a - - - - -] POST http://controller:5000/v3/auth/tokens
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core [req-98982a97-90ca-411f-843d-c4dd5186fe5a - - - - -] Could not find user: root
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core Traceback (most recent call last):
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core   File "/usr/lib/python2.7/dist-packages/keystone/auth/plugins/core.py", line 173, in _validate_and_normalize_auth_data
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core     user_name, domain_ref['id'])
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core   File "/usr/lib/python2.7/dist-packages/keystone/common/manager.py", line 124, in wrapped
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core     __ret_val = __f(*args, **kwargs)
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core   File "/usr/lib/python2.7/dist-packages/keystone/identity/core.py", line 433, in wrapper
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core     return f(self, *args, **kwargs)
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core   File "/usr/lib/python2.7/dist-packages/keystone/identity/core.py", line 443, in wrapper
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core     return f(self, *args, **kwargs)
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core   File "/usr/lib/python2.7/dist-packages/dogpile/cache/region.py", line 1053, in decorate
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core     should_cache_fn)
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core   File "/usr/lib/python2.7/dist-packages/dogpile/cache/region.py", line 657, in get_or_create
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core     async_creator) as value:
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core   File "/usr/lib/python2.7/dist-packages/dogpile/core/dogpile.py", line 158, in __enter__
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core     return self._enter()
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core   File "/usr/lib/python2.7/dist-packages/dogpile/core/dogpile.py", line 98, in _enter
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core     generated = self._enter_create(createdtime)
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core   File "/usr/lib/python2.7/dist-packages/dogpile/core/dogpile.py", line 149, in _enter_create
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core     created = self.creator()
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core   File "/usr/lib/python2.7/dist-packages/dogpile/cache/region.py", line 625, in gen_value
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core     created_value = creator()
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core   File "/usr/lib/python2.7/dist-packages/dogpile/cache/region.py", line 1049, in creator
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core     return fn(*arg, **kw)
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core   File "/usr/lib/python2.7/dist-packages/keystone/identity/core.py", line 902, in get_user_by_name
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core     ref = driver.get_user_by_name(user_name, domain_id)
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core   File "/usr/lib/python2.7/dist-packages/keystone/identity/backends/sql.py", line 253, in get_user_by_name
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core     raise exception.UserNotFound(user_id=user_name)
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core UserNotFound: Could not find user: root
2017-07-30 17:20:29.083 3278 ERROR keystone.auth.plugins.core 
2017-07-30 17:20:29.089 3278 WARNING keystone.common.wsgi [req-98982a97-90ca-411f-843d-c4dd5186fe5a - - - - -] Authorization failed. The request you have made requires authentication. from 172.16.1.5
2017-07-30 17:20:35.852 3279 INFO keystone.common.wsgi [req-2b0ef7e5-a560-4bdd-9815-a7b554fbebb6 - - - - -] POST http://controller:5000/v3/auth/tokens
2017-07-30 17:20:35.957 3279 INFO keystone.token.providers.fernet.utils [req-2b0ef7e5-a560-4bdd-9815-a7b554fbebb6 - - - - -] Loaded 2 encryption keys (max_active_keys=3) from: /etc/keystone/fernet-keys/
2017-07-30 17:20:35.967 3280 INFO keystone.token.providers.fernet.utils [req-299cb3c0-2c36-492d-92d7-4d50f0e5ed55 - - - - -] Loaded 2 encryption keys (max_active_keys=3) from: /etc/keystone/fernet-keys/
2017-07-30 17:20:36.010 3280 INFO keystone.common.wsgi [req-299cb3c0-2c36-492d-92d7-4d50f0e5ed55 63dee1ed626b4040bcd43b3492997a8c - - 19b6c35443a340c5a8648c97c46fdff7 -] POST http://controller:5000/v3/auth/tokens
2017-07-30 17:20:36.016 3280 INFO keystone.token.providers.fernet.utils [req-299cb3c0-2c36-492d-92d7-4d50f0e5ed55 63dee1ed626b4040bcd43b3492997a8c - - 19b6c35443a340c5a8648c97c46fdff7 -] Loaded 2 encryption keys (max_active_keys=3) from: /etc/keystone/fernet-keys/
2017-07-30 17:20:36.097 3280 WARNING keystone.common.wsgi [req-299cb3c0-2c36-492d-92d7-4d50f0e5ed55 63dee1ed626b4040bcd43b3492997a8c - - 19b6c35443a340c5a8648c97c46fdff7 -] Authorization failed. The request you have made requires authentication. from 172.16.1.5
2017-07-30 17:20:36.108 3278 INFO keystone.common.wsgi [req-4964e49e-5345-4baa-b74a-84198dc9dfb0 - - - - -] GET http://controller:5000/v3/
2017-07-30 17:20:36.120 3277 INFO keystone.token.providers.fernet.utils [req-78b59c40-4bc8-4991-8fcb-f7b66c2513a7 - - - - -] Loaded 2 encryption keys (max_active_keys=3) from: /etc/keystone/fernet-keys/
2017-07-30 17:20:36.171 3277 INFO keystone.common.wsgi [req-78b59c40-4bc8-4991-8fcb-f7b66c2513a7 63dee1ed626b4040bcd43b3492997a8c - - 19b6c35443a340c5a8648c97c46fdff7 -] GET http://controller:5000/v3/users/63dee1ed626b4040bcd43b3492997a8c/projects
2017-07-30 17:20:36.219 3278 INFO keystone.token.providers.fernet.utils [req-8487814f-ba80-4ecd-a691-f9d7185e11be - - - - -] Loaded 2 encryption keys (max_active_keys=3) from: /etc/keystone/fernet-keys/
2017-07-30 17:20:36.263 3278 INFO keystone.common.wsgi [req-8487814f-ba80-4ecd-a691-f9d7185e11be 63dee1ed626b4040bcd43b3492997a8c - - 19b6c35443a340c5a8648c97c46fdff7 -] POST http://controller:5000/v3/auth/tokens
2017-07-30 17:20:36.277 3278 INFO keystone.token.providers.fernet.utils [req-8487814f-ba80-4ecd-a691-f9d7185e11be 63dee1ed626b4040bcd43b3492997a8c - - 19b6c35443a340c5a8648c97c46fdff7 -] Loaded 2 encryption keys (max_active_keys=3) from: /etc/keystone/fernet-keys/
2017-07-30 17:20:36.388 3278 INFO keystone.token.providers.fernet.utils [req-8487814f-ba80-4ecd-a691-f9d7185e11be 63dee1ed626b4040bcd43b3492997a8c - - 19b6c35443a340c5a8648c97c46fdff7 -] Loaded 2 encryption keys (max_active_keys=3) from: /etc/keystone/fernet-keys/
2017-07-30 17:20:37.038 3281 INFO keystone.token.providers.fernet.utils [req-409620fb-dd6b-493a-9b9f-259943f1564b - - - - -] Loaded 2 encryption keys (max_active_keys=3) from: /etc/keystone/fernet-keys/
2017-07-30 17:20:37.098 3281 INFO keystone.common.wsgi [req-409620fb-dd6b-493a-9b9f-259943f1564b 63dee1ed626b4040bcd43b3492997a8c - - 19b6c35443a340c5a8648c97c46fdff7 -] GET http://controller:5000/v3/users/63dee1ed626b4040bcd43b3492997a8c/projects