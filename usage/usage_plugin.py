"""
plugin(扩展/插件)是jmcomic=2.2.0新引入的机制，
plugin机制可以实现在`特定时间` 回调 `特定插件`，实现灵活无感知的功能增强，
目前仅支持一个时机: after_init，表示在option对象的 __init__ 初始化方法的最后。

下面以内置插件[login]为例：
插件功能：登录JM，获取并保存cookies。
你可以在option配置文件当中，配置如下内容，来实现在 after_init 时机，调用login插件。

plugin:
  after_init: # 时机
    - plugin: login # 插件的key
      kwargs:
          # 下面是给插件的参数 (kwargs)，由插件类自定义
          username: un # 禁漫帐号
          password: pw # 密码

你也可以自定义插件和插件时机
自定义插件时机需要你重写Option类，示例请见 usage_custom
下面演示自定义插件，分为3步:

1. 自定义plugin类
2. 让plugin类生效
3. 使用plugin的key

如果你有好的plugin想法，也欢迎向我提PR，将你的plugin内置到jmcomic模块中

"""

# 1. 自定义plugin类
from jmcomic import JmOptionPlugin, JmModuleConfig, create_option


class MyPlugin(JmOptionPlugin):
    # 指定你的插件的key
    plugin_key = 'myplugin'

    # 覆盖invoke方法，设定方法只有一个参数，名为`hello_plugin`
    def invoke(self, hello_plugin) -> None:
        print(hello_plugin)


# 2. 让plugin类生效
JmModuleConfig.register_plugin(MyPlugin)

# 3. 在配置文件中使用plugin
"""
plugin:
  after_init: # 时机
    - plugin: myplugin # 插件的key
      kwargs:
        hello_plugin: this is my plugin invoke method's parameter # 你自定义的插件的参数
"""

# 当你使用上述配置文件创建option时，
# 在option初始化完成后，你的plugin会被调用，控制台就会打印出 `this is my plugin invoke method's parameter`
option = create_option('xxx')