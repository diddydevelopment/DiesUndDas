import http
import _thread
import led_strip
animation_thread = _thread.start_new_thread(led_strip.animation_rand_rect,[led_strip.get_np(),20,500])


http_server_thread = _thread.start_new_thread(http.http_listen,[])
