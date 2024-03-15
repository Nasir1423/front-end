HTML+CSS 学习参考：https://www.bilibili.com/video/BV1p84y1P7Z5/

# Supplements（day1）

## C/S & B/S 架构

|            C/S架构             |             B/S架构             |
| :----------------------------: | :-----------------------------: |
| Client-Server（客户端-服务器） | Browser-Server（浏览器-服务器） |
|  需要安装；偶尔更新；不跨平台  |  无需安装；无需更新；可跨平台   |

- C/S 架构一般用于**大型专业、安全性要求较高**的应用
- 前端工程师主要开发基于 B/S 架构的**网页**，也涉及**微信小程序开发**、**客户端开发**（React Native 或 uni-app + Vue）、**服务器搭建**（NodeJS）、**数据可视化**（ECHARTS）

## 浏览器

1. 什么是浏览器内核？内核是浏览器的**核心**，用于**处理**浏览器所得到的各种**资源**。

   <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240311113323911.png" alt="image-20240311113323911" style="width: 95%; display: block; margin: 0 auto;" />

2. 五大主流浏览器

   |   浏览器   |          内核           | 问世时间 |
   | :--------: | :---------------------: | :------: |
   | **Chrome** | Blink（before：webkit） |  2008/9  |
   |   Safari   |         webkit          |  2003/1  |
   |     IE     |         Trident         |  1995/8  |
   |  Firefox   |          Gecko          |  2002/9  |
   |   Opera    | Blink（before：Presto） |  1995/4  |

   - 五大浏览器、四大内核
   - 其他浏览器在四大内核的基础上，添加精美 UI 以及实用功能

## 网页

1. 一个**网站** = 一个或多个**网页**。
2. 网页的组成部分/网页标准：网页 = **结构**（HTML） + **表现**（CSS） + **行为**（JavaScript）。

## 编程软件

- 编程软件：VSCode
- 相关扩展：中文语言包、vscode-icons、Live Server
  - vscode-icons 可以修改文件的图标主题
  - Live Server 可以便捷打开 html 文件，以更加贴近项目上线的方式打开（本地创建一个服务器，将当前文件夹下的内容放到服务器中）
    - 源代码出现改动后，浏览器内容可以**自动刷新**
    - 使用 VSCode 打开的必须是**文件夹**
    - 打开的网页必须是**标准的 HTML 结构**，否则无法自动刷新

# HTML4

## 初认识

1. HTML 全称为 **H**yper**T**ext **M**arkup **L**anguage，翻译为**超文本标记语言**。

   - 超文本：与普通文本相比，内容更加丰富，“超”指超链接
   - 标记：将文本变为超文本的符号

2. 发展史

   <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240311124406435.png" alt="image-2024031112446435" style="width: 95%; display: block; margin: 0 auto;" />

## 标签

1. **标签**：又称**元素**，是 HTML 的基本组成单位。

2. 标签的分类：**双标签**和**单标签**。

   <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240311131611972.png" alt="image-20240311131611972" style="width: 65%; display: block; margin: 0 auto;" />

   ```html
   <marquee>悟已往之不谏，知来者之可追</marquee>
   <input>
   ```

3. 标签之间的关系：**并列**关系、**嵌套**关系。

   ```html
   <marquee>
   	悟已往之不谏，知来者之可追
       <input>
   </marquee>
   ```

4. 注意：标签名不区分大小写，但**小写**更规范。

---

1. **标签属性**：是用于给标签提供**附加信息**的键值对。

   <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240311132213118.png" alt="image-20240311132213118" style="width: 45%; display: block; margin: 0 auto;" />

   ```html
   <marquee loop="1" bgcolor="orange">悟已往之不谏，知来者之可追</marquee>
   <input type="password">
   ```

2. 注意

   - 有些特殊的属性**没有属性名，只有属性值**

     ```html
     <input disabled>
     ```

   - 不同的标签有不同的属性，也有一些通用属性

   - 属性名与属性值都是 W3C 预先规定好的

   - 属性名与属性值都不区分大小写，但推荐**小写**

   - 属性值可以用双引号、单引号表示，也可以不写，但推荐**双引号**

   - 标签中如果出现同名属性，**以第一个为准**，后写的会失效

     ```html
     <input type="text" type="password">
     ```

## 基本结构

1. 源代码是怎样渲染成网页的？浏览器先进行格式检查，合法则直接渲染，否则需要对源代码处理后再进行渲染。

   <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240311134207535.png" alt="image-20240311134207535" style="width: 95%; display: block; margin: 0 auto;" />

2. 网页的**基本结构**

   ```html
   <html>
   	<head>
           <title>网页标题</title>
       </head>
       <body>
           ......
       </body>
   </html>
   ```

   - `body` 标签中是要呈现在网页中的内容
   - `head` 标签中的内容不会出现再网页中
   - `head` 标签中的 `title` 标签用于指定网页的标题

3. 网页开发的两大功能（浏览器右键菜单栏）：**检查**、**查看网页源代码**

   - 检查：经过浏览器处理后的源代码
   - 查看网页源代码：程序员编写的源代码

## 注释

1. HTML 的注释以 `<!--` 开始，以 `-->` 结束。

   ```html
   <!-- 这是注释性文字 -->
   ```

2. 注意：注释不可以嵌套使用。

## 文档声明

1. 因为 HTML 有若干版本，因此为了渲染正确，使用**文档声明**告诉浏览器**当前网页的版本**。最新的，也是默认的网页版本是 **HTML5**，其文档声明为 `<!DOCTYPE html>`。

2. 注意：文档声明必须放在**网页的第一行**，在 `html` 标签的外侧。

   ```html
   <!DOCTYPE html>
   <html>
       <head></head>
       <body></body>
   </html>
   ```

## 字符编码

1. 计算机**存储**数据时进行**编码**，**读取**数据时进行**解码**，编码和解码的过程中都遵循一定的规范，即**字符集**。

2. 数据操作需要遵守两项基本原则

   - 存储时，必须采用**合适的**字符集编码。
   - 存储和读取数据时，必须采用**相同的**字符集进行编码和解码。

3. 通过指定字符解码方式，可以让浏览器在渲染 HTML 文件时不出错误。HTML 通过 `meta` 标签的 `charset` 属性指定字符编码，一般使用 `UTF-8` 字符集。

   ```html
   <head>
   	<meta charset="UTF-8"/>
   </head>
   ```

## 语言

1. 设置 HTML 的语言有助于 ①让浏览器显示对应的翻译提示 ②搜索引擎优化。

2. HTML 通过 `html` 标签中的 `lang` 属性设置**网页的语言**。

   | lang 的取值 | 语言     |
   | ----------- | -------- |
   | `zh-CN`     | 简体中文 |
   | `zh-TW`     | 台湾     |
   | `zh`        | 中文     |
   | `en-US`     | 美国英语 |
   | `en-GB`     | 英国英语 |
   | `en`        | 英语     |

   ```html
   <html lang="zh-CN">
   ```

3. `lang` 的参数取值规律为 `lang=语言-国家/地区`。

## 标准结构

```html
<!DOCTYPE html>
<html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <title>网页标题</title>
    </head>
    <body>
        
    </body>
</html>
```

- VSCode 中，可以通过输入 ` ! + 回车` 快速生成 HTML 的标准结构，并且可以通过内置插件 `emmet` 自定义生成结构的属性
- 通过在存放代码的文件夹中存放一个名为 `favicon.ico` 的图片，可以**配置网站图标**

## 排版标签

|   标签    |         含义         | 单/双 |
| :-------: | :------------------: | :---: |
| `h1`~`h6` |         标题         |  双   |
|    `p`    |         段落         |  双   |
|   `div`   | 无含义，用于整体布局 |  双   |

- `h1` 不仅仅表示一级标题，还可以看作是**重要性**的表征，一般只写一个
- [1-排版标签.html](./CODES/1-排版标签.html)

## 语义化标签（day2|22p）

1. **语义化标签**：即用特定的标签，表达特定的含义。这要求我们在使用 HTML 的标签时，关注的应该是**标签的语义**，而不是标签的效果（这一点是由 CSS 来完成的）。如， `h1` 标签的语义为“网页的主要内容”，效果是“文字加粗加大”，我们更应该关注的是前者。
2. 关注标签语义的优点
   - 代码结构清晰，可读性强
   - 有利于 SEO（搜索引擎优化）
   - 方便设备解析（如屏幕阅读器等）

## 块级元素与行内元素

|     块级元素     |       行内元素        |
| :--------------: | :-------------------: |
|     独占一行     |      不独占一行       |
| 如所有的排版标签 | 如 `input`、`span` 等 |

- **块级元素中能写行内元素和块级元素**（ALMOST NOT ALL）
  - `h1`-`h6` 不能相互嵌套
  - `p` 中不能写块级元素
- **行内元素中能写行内元素，但不能写块级元素**

## 文本标签（常用）

|   标签   |               语义               | 单/双 |
| :------: | :------------------------------: | :---: |
|   `em`   |        需要着重阅读的内容        |  双   |
| `strong` | 十分重要的内容（比 `em` 更重要） |  双   |
|  `span`  | 无语义，是用于包裹短语的通用容器 |  双   |

- 文本标签用于包括词汇、短语等内容
- 文本标签通常写在排版标签里边
- 排版标签关注于大段的文字，而文本标签关注词汇、短语等内容
- 文本标签通常都是**行内元素**
- 排版标签中的 `div` 和文本标签中的 `span` 类似，都没有语义，是更加通用的标签

## 文本标签（不常用）

|     标签     |                             语义                             | 单/双 |
| :----------: | :----------------------------------------------------------: | :---: |
|    `cite`    |               （书籍、歌曲、电影等的）作品标题               |  双   |
|    `dfn`     |                      特殊术语或专有名词                      |  双   |
| `del`/`ins`  |                    删除的文本/插入的文本                     |  双   |
| `sub`/`sup`  |                      下标文字/上标文字                       |  双   |
|    `code`    |                            代码片                            |  双   |
|    `samp`    |   从正常上下文中，将某些内容提取出来（如，标识设备的输出）   |  双   |
|    `kdb`     |              键盘文本，表示文本是通过键盘输入的              |  双   |
|    `abbr`    |                缩写，常配合 `title` 属性使用                 |  双   |
|    `bdo`     |   更改文本方向，常配合 `dir` 属性使用（`dir`=`ltr`/`rtl`）   |  双   |
|    `var`     |      变量，可以与 `code` 标签一起使用（即代码中的变量）      |  双   |
|   `small`    |                附属细则（如，版权、法律文本）                |  双   |
|     `b`      |               摘要中的关键字或评论中的产品名称               |  双   |
|     `i`      |       人物的思想活动、所说的话等；现多用于呈现字体图标       |  双   |
|     `u`      | 表示与正常内容有反差的文本（如，错误的单词、不合适的描述等） |  双   |
|     `q`      |                            短引用                            |  双   |
| `blockquote` |                            长引用                            |  双   |
|  `address`   |                           地址信息                           |  双   |

```html
<abbr title="英雄联盟">LOL</abbr>
<bdo dir="rtl">你是年少的欢喜</bdo>
```

- 上述不常用的文本标签，编写代码时可以不使用
- `blockquote` 和 `address` 是块级元素，其他文本标签都是行内元素
- 语义感不强的标签，如：`small`、`b`、`u`、`q`、`blockquote`，很少使用
- 目前需要记住的**重要的、语义感强**的标签有：`h1`-`h6`、`p`、`div`、`em`、`strong`、`span`

## 图片标签

```html
<img src="", alt="", width="", height="">
<!-- 
1. 标签名：img
2. 语义：图片
3. 常用属性及其含义
	- src 图片路径
	- alt 图片描述
	- width 图片宽度，单位是像素，如 200px
	- height 图片高度，单位是像素，如 200px
4. 单标签
-->
```

- `img` 是一个新的元素分类，即既不属于块级元素，也不属于行内元素，可以暂且认为是行内元素。
- `alt` 属性的作用
  - （最主要）搜索引擎可以通过 `alt` 属性内容，得知图片的内容
  - 当图片无法加载时，有些浏览器会显示 `alt` 属性的值
  - 盲人阅读器等设备会朗读 `alt` 属性的值

## 相对路径与绝对路径

1. **相对路径**：以**当前位置**为参考点去建立路径。

   |        层级        |         相对路径         |
   | :----------------: | :----------------------: |
   |  当前路径（目录）  |           `./`           |
   | 上一级路径（目录） |          `../`           |
   | 上两级路径（目录） |         `../../`         |
   | 下一级路径（目录） |        `./child/`        |
   | 下两级路径（目录） | `./child/2-levels-down/` |

   - 相对路径中的表示当前路径的 `./` 可以省略不写
   - 因为相对路径依赖的是当前位置，如果后期调整了文件位置，那么代码中文件的相对路径也要修改
   - [2-相对路径.html](./CODES/two-levels-up/parent/current/2-相对路径.html)

2. **绝对路径**：以**根位置**（如盘符）为参考点去建立路径。

   - **本地绝对路径**：如 `‪C:\Users\15787\Pictures\GenshinImpactCloudGame\1292433.jpg`，很少使用
     - 一旦更换设备，路径处理起来比较麻烦，因此很少使用
   - **网络绝对路径**：如 `https://www.miyoushe.com/_nuxt/img/miHoYo_Game.2457753.png`
     - 如果服务器开启了防盗链，则会造成图片引入失败

## 常见图片格式

| jpg | png | bmp | gif | webp | base64 |
| :----: | :----: | :----: | :----: | :----: | :------: |
| `.jpg` 或 `.jpeg`，有损压缩，丢弃肉眼不易观察出来的细节 | `.png`，无损压缩，能够更质量的保存图片 | `.bmp`，不进行压缩，最大程度保留图片的更多细节 | `.gif`，仅支持 256 种颜色，色彩呈现不是很完整 | `.webp`，由谷歌推出，专用来在网页中呈现图片 | 本质是一串特殊的文本，需要通过浏览器打开 |
| **支持的颜色丰富** | **支持的颜色丰富** | **支持的颜色丰富，保留的细节更多** | 支持的颜色较少 | 具备前四种格式的优点 | 原理是把图片进行 `base64` 编码，形成一串文本 |
| **占用的空间较小** | 占用空间略大 | 占用空间极大 | | 但是与浏览器的兼容性不好 | 可作为 `img` 标签的 `src` 属性的值 |
| 不支持透明背景 | **支持透明背景** | 不支持透明背景 | **支持简单透明背景** | 使用务必要解决兼容性问题 | |
| 不支持动态图 | 不支持动态图 | 不支持动态图 | **支持动态图** | | |
| 适用于对图片细节**没有极高要求**的场，如：网站的产品宣传图等。 | 适用于①想让图片有透明背景或②想要更高质量地呈现图片，如：公司 logo 图、重要配图等。 | 适用于对图片**细节要求极高**的场景，如：大型游戏中的图片等。 | 适用于网页中的动态图片 | 适用于网页中的各种图片 | 适用于①一些较小的图片②需要和网页一起加载的图片 |

## 超链接

```html
<a href="" target=""></a>
<!--
1. 标签名：a
2. 语义：超链接
3. 常用属性及其含义
	- href 要跳转到的具体位置
	- target 跳转时应该如何打开页面，取值为，
		-- _self 在本页签中打开
		-- _blank 在新页签中打开
4. 双标签
-->
```

[3-超链接.html](./CODES/3-超链接.html)

1. 跳转到**页面**：可以使用 `a` 实现**跳转到其他网页**和**跳转到本地网页**两个功能。

   ```html
   <!-- 超链接-跳转页面 -->
   <!-- 跳转到其他网页 -->
   <a href="https://ys.mihoyo.com/cloud/?utm_source=default#/" target="_blank">云原神，启动！</a>
   <!-- 跳转到本地网页 -->
   <a href="./two-levels-up/parent/current/2-相对路径.html" target="_self">托马照片合集，点击即看！</a>
   ```

   - 代码中的**多个空格和多个回车**，都会被浏览器解析为**一个空格**
   - 虽然 `a` 是行内元素，但是 `a` 可以包裹除自身外的任何元素

2. 跳转到**文件**：可以使用 `a` 实现在浏览器中**打开或下载**文件。

   ```html
   <!-- 超链接-跳转文件 -->
   <!-- 跳转到浏览器可以打开的文件（图片、视频、pdf 等） -->
   <a href="./two-levels-up//托马生日图.jpg">点击查看托马生日照</a>
   <!-- 跳转到浏览器不可以打开的文件（zip 等），会触发自动下载 -->
   <a href="./托马图片合集.7z">点击获取托马照片合集</a>
   <!-- 通过 download 属性，强制触发自动下载，同时可以通过指定取值设定默认下载文件的名称 -->
   <a href="./two-levels-up/托马生日图.jpg" download="托马生日照片">点击下载托马生日照</a>
   ```

   - 浏览器**可以直接打开**的文件，可以通过超链接跳转直接**查看**
   - 浏览器**不可以直接打开**的文件，通过超链接跳转会直接**触发下载**，下载的文件的默认名与 `href` 中的默认名一样
   - 如果想**强制触发下载**要跳转的文件，可以配合使用 `download` 属性，属性值为下载文件的名称（也可以直接通过 `<a href="./two-levels-up/托马生日图.jpg" download>点击下载托马生日照</a>`，省略 `download` 的值后，下载文件的名称默认为 `href` 中的文件名称）
   - 可以跳转到本地文件，也可以跳转到在线文件

3. 跳转到**锚点**：锚点是网页中的一个**标记点**，当通过某种方式设置好锚点后，可以使用 `a` 跳转到**本页面的锚点**或**其他页面的锚点**。

   ```html
   <!-- 超链接-跳转锚点 -->
   <!-- 1. 设置锚点 -->
   <!-- 通过 a 标签的 name 属性设置锚点 -->
   <a name="anchor_a">HHHHHHHHHH</a>
   <!-- 任何标签和 id 属性配合设置锚点 -->
   <h2 id="anchor_h2">这里是一个标定锚点</h2>
   <!-- 2. 跳转锚点 -->
   <!-- 通过 # + 锚点名/id 实现跳转到锚点 -->
   <!-- 通过在超链接的 href 中添加 #，浏览器明白此时的超链接是想要跳转到一个锚点 -->
   <a href="#anchor_a">调转到HHHHHHHHHH</a>
   <a href="#anchor_h2">跳转到“这里是一个标定锚点”</a>
   <a href="./two-levels-up/parent/current/2-相对路径.html#tomma">跳转到“托马比拼图”</a>
   <!-- 3. 其他跳转行为 -->
   <!-- 通过 href="#" 实现跳转到网页顶部 -->
   <a href="#">回到顶部</a>
   <!-- 通过 href="" 刷新页面 -->
   <a href="">刷新</a>
   <!-- 4. JS 弹窗行为 -->
   <a href="javascript:alert('Hello world!');">欢迎世界</a>
   ```

   - **设置锚点**有两种方式：① `a` 标签配合 `name` 属性 ② 任意标签配合 `id` 属性
   - 具有 `href` 属性的 `a` 标签是**超链接**；具有 `name` 属性的 `a` 标签是**锚点**
   - `name` 和 `id` 都是**区分大小写**的，其中 `id` 最好不要是数字开头
   - **跳转锚点**分为两种情况：①跳转到本页面中的锚点，此时 `href` 取值为 `#name值` 或 `#id值` ②跳转到其他页面中的锚点，此时 `href` 取值为 `其他页面的路径#name值` 或 `其他页面的路径#id值`
   - 网页中的导航栏可以通过锚点来实现
   - **回到当前网页顶部**和**刷新当前网页**可以通过 `<a href="#"></a>` 和 `<a href=""></a>` 来实现
   - **执行一段 js 代码**可以通过 `<a href="javascript:这里是 js 代码;"></a>` 来实现

4. **唤起指定应用**：可以使用 `a` 标签唤起设备应用程序。

   ```html
   <!-- 超链接-唤起指定应用 -->
   <!-- 唤起电话拨号 -->
   <a href="tel:10086">给 10086 拨打电话</a>
   <!-- 唤起短信发送短信 -->
   <a href="sms:10086">给 10086 发送短信</a>
   <!-- 唤起邮箱发送邮件 -->
   <a href="mailto:10000@qq.com">给 10000@qq.com 发送邮件</a>
   ```

5. 什么是**超文本**？超文本是一种组织信息的方式，通过超链接将不同空间的文字、图片等各种信息组织在一起，能从当前阅读的内容，跳转到超链接所指向的内容（页面、文件、锚点、应用）。

## 列表（day3|35p）

[4-列表.html](./CODES/4-列表.html)

1. **有序**列表：有顺序或侧重顺序的列表。

   ```html
   <h2>红烧肉的做法如下</h2>
   <ol>
       <li>准备材料，五花肉洗净，切成麻将块大小；</li>
       <li>锅烧热放火麻油，爆香姜片大蒜花椒八角；</li>
       <li>倒入五花肉翻炒至两面微焦，加入料酒或者白酒、酱油、冰糖；</li>
       <li>转入砂锅加适量开水，慢火焖一个小时，要注意经常翻身，一方面均匀上色，另一方面避免猪皮粘锅。出锅之前撒点胡椒粉和盐就可以了。</li>
   </ol>
   ```

   - `<ol>` 和 `<li>` 配合使用构成有序列表
   - ol=ordered list，li=list item，`<ol>` 表示有序列表，`<li>` 表示列表项
   - `<ol></ol>` 中只能放 `<li></li>`

2. **无序**列表：无顺序或不侧重顺序的列表。

   ```html
   <h2>西安旅游推荐景点如下</h2>
   <ul>
       <li>大雁塔</li>
       <li>华清池</li>
       <li>不夜城</li>
       <li>钟楼</li>
   </ul>
   ```

   - `<ul>` 和 `<li>` 配合使用构成无序列表
   - ul=unordered list，li=list item，`<ul>` 表示无序列表，`<li>` 表示列表项
   - `<ul></ul>` 中只能放 `<li></li>`

3. **自定义**列表：包含**术语名**称以及**术语描述**的列表。

   ```html
   <h2>前端术语解释</h2>
   <dl>
       <dt>HTML</dt>
       <dd>HTML 的全称是 HyperText Markup Language</dd>
       <dd>HTML 中最重要的标签之一是 a</dd>
   
       <dt>CSS</dt>
       <dd>CSS 的全称是 Cascading Style Sheets</dd>
       <dd>HTML 相当于网页的骨架，CSS 则对网页进行修饰</dd>
   </dl>
   ```

   - `<dl>`、`<dt>` 和 `<dd>` 配合使用构成自定义列表
   - dl=definition list，dt=definition term，dd=definition description，`<dl>` 表示自定义列表，`<dt>` 表示术语名称，`<dd>` 表示术语描述
   - 一个 `<dt>` 可以搭配多个 `<dd>` 使用

4. 列表**嵌套**：列表中的某项（item），又包含了一个列表。

   ```html
   <h2>我想去的几个城市</h2>
   <ul>
       <li>成都</li>
       <li>重庆</li>
       <li>
           <span>北京</span>
           <ul>
               <li>天安门</li>
               <li>圆明园</li>
               <li>颐和园</li>
               <li>故宫</li>
           </ul>
       </li>
       <li>上海</li>
   </ul>
   ```

   - `<li>` 标签最好写在 `<ul>` 或 `<ol>` 中 ，不要单独使用

## 表格

[5-表格.html](./CODES/5-表格.html)

### 基本结构

一个完整的表格由**表格标题、表格头部、表格主体、表格脚注**四部分组成。

|   标签    |               语义               |
| :-------: | :------------------------------: |
|  `table`  |               表格               |
| `caption` |             表格标题             |
|  `thead`  |             表格头部             |
|  `tbody`  |             表格主体             |
|  `tfoot`  |             表格脚注             |
|   `tr`    |                行                |
|   `th`    |      （表格头部中的）单元格      |
|   `td`    | （表格主体和表格脚注中的）单元格 |

<img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240313134302117.png" alt="image-20240313134302117" style="width: 55%; display: block; margin: 0 auto;" />

- **表格**：`<table></table>`

  ```html
  <table>
      <caption></caption>
      <thead></thead>
      <tbody></tbody>
      <tfoot></tfoot>
  </table>
  ```

- **表格标题**：`<caption></caption>`

  ```html
  <caption>学生信息</caption>
  ```

- **表格头部**：`<thead></thead>`

  ```html
  <thead>
  	<tr>
          <th>姓名</th>
          <th>性别</th>
          <th>年龄</th>
          <th>民族</th>
          <th>政治面貌</th>
      </tr>
  </thead>
  ```

  <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240313134538679.png" alt="image-20240313134538679" style="width: 65%; display: block; margin: 0 auto;" />

- **表格主体**：`<tbody></tbody>`

  ```html
  <tbody>
      <tr>
          <th>张三</th>
          <th>男</th>
          <th>18</th>
          <th>汉族</th>
          <th>团员</th>
      </tr>
      <tr>
          <th>李四</th>
          <th>女</th>
          <th>20</th>
          <th>满族</th>
          <th>群众</th>
      </tr>
  </tbody>
  ```

  <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240313135123697.png" alt="image-20240313135123697" style="width: 65%; display: block; margin: 0 auto;" />

- **表格脚注**：`<tfoot></tfoot>`

### 常用属性

|  标签   |    语义    |                           常用属性                           | 单/双 |
| :-----: | :--------: | :----------------------------------------------------------: | :---: |
| `table` |    表格    | `width` 表格宽度<br />`height` 表格**最小**高度<br />`border` 表格边框宽度<br />`cellspacing` 单元格之间的间距 |  双   |
| `thead` |  表格头部  | `height` 表格头部高度<br />`align` 单元格的水平对齐方式，可选值为：`left`、`center`、`right`<br />`valign` 单元格的垂直对齐方式，可选值为：`top`、`middle`、`bottom` |  双   |
| `tbody` |  表格主体  |                          同 `thead`                          |  双   |
| `tfoot` |  表格脚注  |                          同 `thead`                          |  双   |
|  `tr`   |     行     |                          同 `thead`                          |  双   |
|  `th`   | 表头单元格 | `width` 单元格宽度<br />`height` 单元格高度<br />`align` 单元格水平对齐方式，取值同 `thead`<br />`valign` 单元格垂直对齐方式，取值同 `thead`<br />`rowspan` 单元格要跨的行数<br />`colspan` 单元格要跨的列数 |  双   |
|  `td`   | 普通单元格 |                           同 `th`                            |  双   |

- `table` 中的 `height` 设置的是**表格的最小高度**，表格最终高度可能比设置的值大
- `table` 中的 `border` 可以控制**表格边框的宽度**，但是无法控制单元格边框的宽度 
- `th` 和 `td` 设置好宽度后，其所在列的宽度就确定了
- `th` 和 `td` 设置好高度后，其所在行的高度就确定了

## 常用标签（补充）

| 标签  |    语义    | 单/双 |
| :---: | :--------: | :---: |
| `br`  |    换行    |  单   |
| `hr`  |    分隔    |  单   |
| `pre` | 按原文显示 |  双   |

- `br` 和  ` hr` 标签，应关注其**语义**，而不是其带来的~~效果~~

## 表单

[6-表单.html](./CODES/6-表单.html)

### 基本结构

|    标签    |       语义       |                             属性                             | 单/双 |
| :--------: | :--------------: | :----------------------------------------------------------: | :---: |
|   `form`   |       表单       | `action` 指定表单的提交地址<br />`target` 控制表单提交后，如何跳转，可取值：`_self`，`blank`<br />`method` 控制表单提交的请求方式，可选值：`get`、`post` |  双   |
|  `input`   |      输入框      | `type` 设置表单控件的类型，可取值：`text`、`password`、`radio`、`checkbox`、`hidden`、`submit`、`reset`、`button`、...<br />`name` 指定提交数据的名称<br />`value` 对于输入框，指定默认输入值的值；对于单选和复选框，是实际提交的数据；对于按钮，是显示在按钮上的文字<br />`maxlength` 对于输入框，设置最大可输入长度<br />`checked` 用于单选和复选框的默认选中 |  单   |
| `textarea` |      文本域      | `name` 数据名称<br />`rows` 默认显示的行数<br />`cols` 默认显示的列数<br />`disabled` 设置表单控件不可用 |  双   |
|  `select`  |      下拉框      |     `name` 数据名称<br />`disabled` 设置整个下拉框不可用     |  双   |
|  `option`  |   下拉框的选项   | `value` 该选项提交的数据（如不指定，将标签中的内容作为提交数据）<br />`selected` 默认选中<br />`disabled` 设置下拉选项不可用 |  双   |
|  `button`  |       按钮       | `type` 设置按钮的类型，可选值：`submit`（默认）、`reset`、`button` |  双   |
|  `label`   | 与表单控件做关联 |                `for` 要关联的表单控件的 `id`                 |  双   |
| `fieldset` |   表单控件分组   |                                                              |  双   |
|  `legend`  | 表单控件分组名称 |                                                              |  双   |

```html
<!-- 以下代码可以实现：点击对应按钮后，到百度或京东搜索文本框中写入的内容 -->
<form action="https://www.baidu.com/s" target="_blank">
    <input type="text" name="wd">
    <button>通过百度搜索</button>
</form>
<form action="https://search.jd.com/search" target="_self">
    <input type="text" name="keyword">
    <button>通过京东搜索</button>
</form>
```

- 表单的提交地址（`form-target`）需要与后端人员沟通后确定，例如百度搜索的提交地址是 `https://www.baidu.com/s`，而京东搜索的提交地址为 `https://search.jd.com/search` 
- 表单的提交方式（`form-method`）会在 `Ajax` 的学习中涉及
- 提交数据的名字（`input-name`）需要与后端人员沟通后确定

### 常用控件

|                 控件                  |    语义    |                           相关属性                           | 单双 |
| :-----------------------------------: | :--------: | :----------------------------------------------------------: | :--: |
|         `<input type="text">`         | 文本输入框 | `name` 数据名称<br />`value` 输入框的默认值<br />`maxlength` 输入框的最大可输入长度 |  单  |
|       `<input type="password">`       | 密码输入框 | `name` 数据名称<br />`value` 输入框的默认值<br />`maxlength` 输入框的最大可输入长度 |  单  |
|        `<input type="radio">`         |   单选框   | `name` 数据名称<br />`value` 提交的数据值<br />`checked` 默认选中该单选框 |  单  |
|       `<input type="checkbox">`       |   复选框   | `name` 数据名称<br />`value` 提交的数据值<br />`checked` 默认选中该复选框 |  单  |
|        `<input type="hidden">`        |   隐藏域   |          `name` 数据名称<br />`value` 提交的数据值           |  单  |
| `<input type="submit" value="提交">`  |  提交按钮  |                    `value` 指定按钮的文字                    |  单  |
| `<button type="submit">提交</button>` |  提交按钮  |                                                              |  双  |
|  `<input type="reset" value="重置">`  |  重置按钮  |                    `value` 指定按钮的文字                    |  单  |
| `<button type="reset">重置</button>`  |  重置按钮  |                                                              |  双  |
| `<input type="button" value="norm">`  |  普通按钮  |                    `value` 指定按钮的文字                    |  单  |
| `<button type="button">norm</button>` |  普通按钮  |                                                              |  双  |
|  `<textarea name="msg"></textarea>`   |   文本域   | `name` 数据名称<br />`rows` 默认显示的行数<br />`cols` 默认显示的列数 |  双  |
|    `<select name="from"></select>`    |   下拉框   |                       `name` 数据名称                        |  双  |
|  `<option value="bj">北京</option>`   | 下拉框的项 |     `value` 提交的数据值<br />`selected` 默认选中该选项      |  双  |

- 密码输入框（`<input type="password">`）一般不使用 `value` 属性，无意义
- 多个单选框（`<input type="radio">`）的 `name` 属性的取值必须相同，才能实现单选功能
- 单选框（`<input type="radio">`）的 `checked` 属性没有值，仅仅表明有该属性的单选框被选中
- 隐藏域（`<input type="hidden">`）是一个用户不可见的区域，其作用是提交表单时，携带一些固定的数据
- 除了 `name` 属性以外，必须指定单选框和复选框的 `value` 属性的值
- 下拉框（`<select name="from"></select>`）中只能写 `option` 标签
- 下拉框的项（`<option value="bj">北京</option>`）最好设置 `value` 值，否则提交的数据就是 `option` 标签中的值
- 下拉框的项（`<option value="bj">北京</option>`）的 `selected` 属性没有值，仅仅表明有该属性的项目被选中

```html
<h2>Person Information Sheet</h2>
<form action="https://search.jd.com/search">
    Account: <input type="text" name="acct" value="admin" maxlength="10"> <br>
    Password: <input type="password" name="pwd" maxlength="8"> <br>
    Gender: 
    <input type="radio" name="gender" value="male" checked>Male
    <input type="radio" name="gender" value="female">Female <br>
    Language:
    <input type="checkbox" name="language" value="c">C
    <input type="checkbox" name="language" value="java">Java
    <input type="checkbox" name="language" value="python" checked>Python <br>
    <input type="hidden" name="from" value="jd"> 
    Preferred Salary:
    <select name="salary">
        <option value="level-1">10k+</option>
        <option value="level-2">13k+</option>
        <option value="level-3" selected>15k+</option>
        <option value="level-4">18k+</option>
    </select> <br>
    Self-Assessment:
    <textarea name="msg" cols="12" rows="3">Make a assessment of yourself here</textarea> <br>
    <button type="submit">confirm</button>
    <button type="reset">reset</button>
    <button type="button">verify</button>
</form>
```

### 禁用控件

给表单控件的标签添加 `disabled` 属性可以**禁用该控件**，禁用后用户将无法在网页中对其进行操作。

### label 标签（控件关联）

1. `label` 标签可以将文字（或其他内容）与表单控件**相关联**。关联之后，点击文字，与之对应的表单控件就会获取焦点。

2. 关联方式

   - 给表单控件设置 `id` 属性，并且让 `label` 标签的 `for` 属性的值等于表单控件的 `id` 属性的值

     ```html
     <label for="act">
         Account: 
     </label>
     <input id="act" type="text" name="acct" value="admin" maxlength="10"> <br>
     ```

   - 将表单控件和文字（或其他内容）整体放在 `label` 标签里边

     ```html
     <label>
         Password: <input type="password" name="pwd" maxlength="8">
     </label> <br>
     ```

### fieldset/legend 标签（控件分组）

- `fieldset` 标签为表单控件**分组**，`legend` 标签设置分组的**标题**

```html
<h2>Person Information Sheet</h2>
<form action="https://search.jd.com/search">
    <fieldset>
        <legend>Majority</legend>
        <label for="act">
            Account:
        </label>
        <input id="act" type="text" name="acct" value="admin" maxlength="10"> <br>
        <label>
            Password: <input type="password" name="pwd" maxlength="8">
        </label> <br>
        Gender:
        <input type="radio" name="gender" value="male" checked>Male
        <input type="radio" name="gender" value="female">Female <br>
        Language:
        <input type="checkbox" name="language" value="c">C
        <input type="checkbox" name="language" value="java">Java
        <input type="checkbox" name="language" value="python" checked>Python <br>
        <input type="hidden" name="from" value="jd">
    </fieldset>
    <fieldset>
        <legend>Supplement</legend>
        Preferred Salary:
        <select name="salary">
            <option value="level-1">10k+</option>
            <option value="level-2">13k+</option>
            <option value="level-3" selected>15k+</option>
            <option value="level-4">18k+</option>
        </select> <br>
        Self-Assessment:
        <textarea name="msg" cols="12" rows="3">Make a assessment of yourself here</textarea> <br>
    </fieldset>


    <button type="submit">confirm</button>
    <button type="reset">reset</button>
    <button type="button">verify</button>
</form>
```

## 框架标签

[7-框架标签.html](./CODES/7-框架标签.html)

```html
<iframe src="" name="" width="" height="" frameborder=""></iframe>
<!-- 
1. 标签名：iframe
2. 语义：框架
3. 常用属性及其含义
    - name 框架名字，可以与 target 属性配合使用
    - width 框架的宽度
    - height 框架的高度
    - frameborder 是否显示边框，可取值：0 或 1
4. 双标签
5. 应用
	- 在网页中嵌入一个普通网页/广告网页
	- 在网页中嵌入一个浏览器可以打开的文件（图片、视频、pdf 等）
	- 将 iframe 的 name 与超链接或表单的 target 配合，实现：超链接点击或表单提交后跳转到网页中嵌入的 iframe 框架中
-->
```

```html
<h2>通过 iframe 嵌入一个普通网页</h2>
<iframe src="https://www.bilibili.com" frameborder="1" width="600" height="300"></iframe>
<br>

<h2>通过 iframe 嵌入一个广告网页</h2>
<iframe src="https://pic3.zhimg.com/v2-8065c386354970c985325383711b337f_720w.webp?source=d6434cab" frameborder="1" width="600" height="300"></iframe>
<br>

<h2>通过 iframe 嵌入浏览器可以打开的文件（图片、视频、pdf 等）</h2>
<iframe src="./two-levels-up/托马生日图.jpg" frameborder="1" width="600" height="300"></iframe>

<h2>通过 iframe 的 name 属性与表单或超链接的 target 属性关联，可以让超链接（或表单提交后）要跳转的页面在 iframe 框架中打开</h2>
<a href="https://www.bilibili.com" target="container">点击访问哔哩哔哩</a>
<a href="https://www.taobao.com" target="container">点击访问淘宝</a> <br>
<form action="https://search.jd.com/search" target="container">
    <label for="txt">
        在京东商城搜索商品
    </label>
    <input type="text" name="keyword" id="txt">
    <input type="submit" value="搜索">
</form>
<iframe name="container" frameborder="1" width="600" height="300"></iframe>
```

## 字符实体

1. HTML **实体**：在 HTML 中，某些字符是预留的，如 <、>，如果想要**正确显示预留字符**，则必须在 HTML 源代码中使用**字符实体**（character entities）。

2. 字符实体的形式：`&实体名称;` 或 `&#实体编号;`

3. 常见的字符实体（详细的字符实体的名称或编号见 [HTML Standard](https://html.spec.whatwg.org/multipage/named-characters.html#named-character-references)）

   | 显示结果 | 描述              | 实体名称          | 实体编号 |
   | :------: | :---------------: | :---------------: | :------: |
   |          | **空格**          | `&nbsp;`          | `&#160;`  |
   | <        | **小于号**        | `&lt;`            | `&#60;`    |
   | >        | **大于号**        | `&gt;`              | `&#62;`    |
   | &        | **和号**          | `&amp;`             | `&#38;`    |
   | "        | 引号              | `&quot;`            | `&#34;`    |
   | '        | 撇号              | `&apos;` (IE不支持) | `&#39;`    |
   | ￠       | 分（cent）        | `&cent;`            | `&#162;`   |
   | £        | 镑（pound）       | `&pound;`           | `&#163;`   |
   | ¥        | **元**（yen）     | `&yen;`             | `&#165;`   |
   | €        | 欧元（euro）      | `&euro;`            | `&#8364;`  |
   | §        | 小节              | `&sect;`            | `&#167;`   |
   | ©        | **版权**（copyright） | `&copy;`            | `&#169;`   |
   | ®        | 注册商标          | `&reg;`             | `&#174;`   |
   | ™        | 商标              | `&trade;`           | `&#8482;`  |
   | ×        | **乘号**          | `&times;`           | `&#215;`   |
   | ÷        | **除号**          | `&divide;`          | `&#247;`   |

## 全局属性

**全局属性**是所有 HTML 元素**共有**的属性，它们可以用于所有元素，即使属性可能对某些元素不起作用。（关于全局属性的详细信息见 [全局属性 - HTML（超文本标记语言） | MDN](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Global_attributes)）

| 全局属性 |                      含义                      |
| :------: | :--------------------------------------------: |
|   `id`   |               标签的**唯一**标识               |
| `class`  |                 标签的**类名**                 |
| `style`  |     **内联样式**，直接给标签指定 CSS 样式      |
|  `dir`   |  指定标签中**文本方向**，可取值 `ltr`、`rtl`   |
| `title`  | 给标签设置一个**文字提示**，多用于超链接和图片 |
|  `lang`  |             指定标签内容的**语言**             |

## meta 标签

`<meta>` 标签用于配置网页**元信息**（基本信息）。

|                             代码                             |             含义             |
| :----------------------------------------------------------: | :--------------------------: |
|                   `<meta charset="utf-8">`                   |         配置字符编码         |
|   `<meta http-equiv="X-UA-Compatible" content="IE=edge">`    | 针对 `IE` 浏览器的兼容性配置 |
| `<meta name="viewport" content="width=device-width, initial-scale=1.0">` |       针对移动端的配置       |
| `<meta name="keywords" content="8-12个以英文逗号隔开的单词/词语">` |        配置网页关键字        |
| `<meta name="description" content="80字以内的一段话，与网站内容相关">` |      配置网页描述性信息      |
| `<meta name="robots" content="针对不同情况，有不同的特定取值">` |     针对搜索引擎爬虫配置     |
|            `<meta name="author" content="tony">`             |         配置网页作者         |
|         `<meta name="generator" content="VS Code">`          |       配置网页生成工具       |
|      `<meta name="copyright" content="2023-2027©所有">`      |         配置版权信息         |
| `<meta http-equiv="refresh" content="10;url=https://www.baidu.com">` |       配置网页自动刷新       |

## SUMMARY of HTML4

**HTML4 标签**

<img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/HTML4%20%E6%A0%87%E7%AD%BE.svg" alt="HTML4 标签" style="width: 85%; display: block; margin: 0 auto;" />

**HTML4 其他**

<img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/HTML4%20%E5%85%B6%E4%BB%96.svg" alt="HTML4 其他" style="width: 80%; display: block; margin: 0 auto;" />

# CSS2

## 初认识

1. CSS 全称为 **C**ascading **S**tyle Sheets，翻译为**层叠样式表**。
   - 层叠：CSS 给 HTML 设置样式像化妆一样，是一层一层的
   - 样式：文字大小、颜色、元素宽高等
   - 表：列表
2. HTML 负责结构，CSS 添加样式，二者实现了**结构与样式的分离**。

## 编写位置

### 行内样式

1. **行内样式**：又称为**内联样式**，是写在标签的 `style` 属性中的样式表。

   ```html
   <h1 style="color: red; font-size: 60px">悟已往之不谏，知来者之可追</h1>
   ```

   - `style` 属性的值要符合 **CSS 语法规范**，即 `名:值;` 的形式
   - 行内样式表只能控制当前标签的样式，对其他标签无效

2. 不足之处

   - 书写繁琐、样式**不能复用**
   - **无法体现结构与样式分离的思想**
   - 只有对当前元素添加简单样式时，才偶尔使用，不推荐大量使用

### 内部样式

1. **内部样式**：是写在 HTML 页面内部，将所有 CSS 代码提取出来，单独放在 `style` 标签中的样式表。

   ```html
   <head>
       <style>
           h1 {
               color: red;
               font-size: 40px;
           }
   	</style>
   </head>
   <body>
       <h1 style="color: red; font-size: 60px">悟已往之不谏，知来者之可追</h1>
   </body>
   ```

   - `style` 标签理论上可以放在 HTML 文档的任何地方，但一般都**放在 `head` 标签**中

2. 优点与不足之处

   - 优点：样式**可以复用**、代码结构清晰
   - 不足之处
     - **没有实现结构与样式完全分离**
     - 多个 HTML 页面无法服用样式

### 外部样式

1. **外部样式**：单独写在 `.css` 文件中，随后在 HTML 文件中通过 `link` 标签引入使用的样式表。

   ```css
   /* CSS 文件(xxx.css)  */
   h1 {
       color: red;
       font-size: 40px;
   }
   ```

   ```html
   <!-- HTML 文件 -->
   <head>
   	<link rel="stylesheet" href="./xxx.css">
   </head>
   <body>
       <h1 style="color: red; font-size: 60px">悟已往之不谏，知来者之可追</h1>
   </body>
   ```

   - `link` 标签要写在 `head` 标签中
   - `<link rel="" href="">`
     - `rel` 是 relation 的缩写，说明引入的文档与当前文档之间的关系
     - `href` 指定要引入的文档的位置

2. 优点

   - 样式**可以复用**、结构清晰
   - **可触发浏览器的缓存机制**，提高访问速度
   - 实现了**结构与样式的完全分离**
   - 实际开发中，几乎都使用外部样式，是**最推荐**的使用方式

## 样式表优先级

1. 优先级规则：**行内样式** > **内部样式** = **外部样式**

   - 内部样式、外部样式优先级相同，并且**后来的样式会覆盖掉前面的同名样式**

     ```css
     /* CSS 文件(xxx.css) */
     h1 {
         color: red;
         font-size: 60px;
     }
     ```

     ```html
     <!-- HTML 文件 -->
     <head>
     	<link rel="stylesheet" href="./xxx.css">
         <style>
             h1 {
                 color: green;
             }
         </style>
     </head>
     <body>
         <h1 style="color: red; font-size: 60px">悟已往之不谏，知来者之可追</h1>
     </body>
     <!-- 网页上的文字样式应该是 green 60px -->
     ```

   - 同一个样式表中，**后来的样式也会覆盖掉前面的同名样式**

     ```html
     <h1 style="color: red; font-size: 60px; color: green">悟已往之不谏，知来者之可追</h1>
     <!-- 网页上的文字样式应该是 green 60px -->
     ```

2. 三种样式表的对比

   |              | **行内样式**                                         | **内部样式**                                 | **外部样式**                                                 |
   | ------------ | ---------------------------------------------------- | -------------------------------------------- | ------------------------------------------------------------ |
   | **优点**     | 优先级最高                                           | 样式可复用<br />代码结构清晰                 | 样式可多页面复用<br />代码结构清晰<br />可触发浏览器缓存机制<br />结构与样式彻底分离 |
   | **缺点**     | 结构与样式未分离<br />代码结构混乱<br />样式不能复用 | 结构与样式未彻底分离<br />样式不能多页面复用 | 需要引入才能使用                                             |
   | **使用频率** | 使用频率很低                                         | 一般                                         | 最高                                                         |
   | **作用范围** | 当前标签                                             | 当前页面                                     | 多个页面                                                     |

## 语法规范

1. CSS 样式由两部分组成：**选择器**和**声明块**

   - **选择器**：负责找到要添加样式的元素

   - **声明块**：负责设置具体的样式，由一个或多个**声明**组成（声明的格式为：`属性名: 属性值;`）

   <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240314001835136.png" alt="image-20240314001835136"  style="width: 50%; display: block; margin: 0 auto;" />

2. 注意

   - 声明块中的最后一个声明的分号可以省略，但推荐写上
   - 选择器与声明块之间，属性名与属性值之间，均有一个空格，可以省略，但推荐写上

## 注释

CSS 的注释以 `/*` 开始，以 `*/` 结束。

```css
/* 这是注释性文字 */
```

## 代码风格

- **展开风格**：开发时推荐使用，便于维护和调试

  ```html
  h1 {
  	color: red;
  	font-size: 40px;
  }
  ```

- **紧凑风格**：项目上线时使用，可以减小文件体积

  ```html
  h1{color:red;font-size:40px}
  ```

## 基本选择器

[8-基本选择器](./CODES/8-基本选择器.html)

| 基本选择器 |      语法      |                     特点                     |
| :--------: | :------------: | :------------------------------------------: |
| 通配选择器 |      `*`       |                 选中所有标签                 |
| 元素选择器 | `element-name` |         选中  `element-name` 的标签          |
|  类选择器  | `.class-name`  | 选中类名为 `class-name` 的标签（使用频率高） |
| id 选择器  |  `#id-value`   |      选中 id 值为 `id-value` 的单个标签      |

### 通配选择器

1. **通配选择器**：`*`，可以选择页面中的**所有 HTML 元素**。

2. **语法**

   ```css
   * {
   	属性名1: 属性值1;
       属性名2: 属性值2;
       ...
       属性名n: 属性值n;
   }
   ```

3. 注意：通配选择器在清楚样式时有很大作用。

### 元素选择器

1. **元素选择器**：`标签名`，可以选择页面中的**特定标签的所有元素**。

2. **语法**

   ```css
   标签名 {
       属性名1: 属性值1;
       属性名2: 属性值2;
       ...
       属性名n: 属性值n;
   }
   ```

3. 注意：元素选择器的缺点是无法实现差异化设置。

### 类选择器

1. **类选择器**：`.类名`，可以选择页面中的有特定 `class` 值（**类名**）的所有元素。

2. **语法**

   ```css
   .类名 {
       属性名1: 属性值1;
       属性名2: 属性值2;
       ...
       属性名n: 属性值n;
   }
   ```

3. 注意

   - 元素的 `class` 值是我们自定义的，一般来说，不要使用纯数字、不要使用中文、**尽量使用英文与数字的组合，若由多个单词组成，使用 `-` 做连接**

   - 一个元素**不能写多个 `class` 属性**，但是一个元素的 `class` 属性**可以写多个值**，用空格隔开

     ```html
     <!-- 错误示例 -->
     <h1 class="motto" class="quote">悟已往之不谏，知来者之可追</h1>
     <!-- 正确示例 -->
     <h1 class="motto quote">悟已往之不谏，知来者之可追</h1>
     ```

### id 选择器

1. **id 选择器**：`#id值`，可以**精准**选中页面中**某个**有特定 `id` 值的元素。

2. **语法**

   ```css
   #id值 {
       属性名1: 属性值1;
       属性名2: 属性值2;
       ...
       属性名n: 属性值n;
   }
   ```

3. 注意

   - 元素的 `id` 值尽量由**字母、数字、下划线（_）、短横线（-）**组成，最好以字母开头，不要包含空格，**区分大小写**
   - 一个元素只能拥有一个 `id` 属性，多个元素的 `id` 属性值不能相同
   - 一个元素可以同时拥有 `id` 值和 `class` 属性

## 复合选择器

[9-复合选择器（交并集）](./CODES/9-复合选择器（交并集）.html)

[10-复合选择器（子后代、兄弟）](./CODES/10-复合选择器（子后代、兄弟）.html)

[11-复合选择器（属性）](./CODES/11-复合选择器（属性）.html)

[12-复合选择器（动态伪类）](./CODES/12-复合选择器（动态伪类）.html)

[13-复合选择器（结构伪类-常用）](./CODES/13-复合选择器（结构伪类-常用）.html)

[14-复合选择器（其他伪类）](./CODES/14-复合选择器（其他伪类）.html)

[15-复合选择器（伪元素）](./CODES/15-复合选择器（伪元素）.html)

| 复合选择器 |                        语法                        |                        特点                        |
| :--------: | :------------------------------------------------: | :------------------------------------------------: |
| 交集选择器 |        `selector_1selector_2...selector_n`         |           选中 n 个选择器选中的元素交集            |
| 并集选择器 |       `selector_1,selector_2,...,selector_n`       |           选中 n 个选择器选中的元素并集            |
| 后代选择器 |       `selector_1 selector_2 ... selector_n`       |          选中指定元素中符合要求的后代元素          |
| 子代选择器 |       `selector_1>selector_2>...>selector_n`       |          选中指定元素中符合要求的子代元素          |
| 兄弟选择器 | `selector_1+selector_2` or `selector_1~selector_2` | 选中指定元素的一个下方直接相邻兄弟 or 所有下方兄弟 |
| 属性选择器 |            `[属性名="属性值"]` or more             |         选中具有某个属性且具有特定值的元素         |
| 伪类选择器 |            动态伪类、结构伪类、否定伪类            |                                                    |

### 交集选择器

1. **交集选择器**：`selector_1selector_2...selector_n`，可以选择**同时符合多个条件**的元素。

2. **语法**

   ```css
   selector_1selector_2...selector_n {
       属性名1: 属性值1;
       属性名2: 属性值2;
       ...
       属性名n: 属性值n;
   }
   ```

3. 注意

   - 如果元素选择器是交集选择器的一部分，则元素选择器必须写在最前面
   - id 选择器也可以作为交集选择器的一部分，但是实际应用中几乎不用，没有任何意义
   - 交集选择器中不可能出现两个元素选择器
   - **元素选择器配合类名选择器**是用的最多的交集选择器

### 并集选择器

1. **并集选择器**：`selector_1,selector_2,...,selector_n`，可以选择**符合任意条件**的元素。

2. **语法**

   ```css
   selector_1,
   selector_2,
   ...,
   selector_n {
       属性名1: 属性值1;
       属性名2: 属性值2;
       ...
       属性名n: 属性值n;
   }
   ```

3. 注意

   - 任何选择器都可以作为并集选择器的一部分
   - 并集选择器通常用于**集体声明**，可以缩小样式表的体积

### 元素之间的关系

|                            关系                            |                             图示                             |
| :--------------------------------------------------------: | :----------------------------------------------------------: |
| **父元素**：**直接**包裹某个元素的元素，就是该元素的父元素 | <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240314022224882.png" alt="image-20240314022224882" style="width: 50%; display: block; margin: 0 auto;" /> |
|     **子元素**：被父元素**直接**包裹的元素（儿子元素）     | <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240314022348148.png" alt="image-20240314022348148" style="width: 50%; display: block; margin: 0 auto;"  /> |
|     **祖先元素**：父亲的父亲……，一直向外找，都是祖先。     | <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240314022619496.png" alt="image-20240314022619496" style="width: 50%; display: block; margin: 0 auto;" /> |
|     **后代元素**：儿子的儿子……，一直向里找，都是后代。     | <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240314022704237.png" alt="image-20240314022704237" style="width: 50%; display: block; margin: 0 auto;" /> |
|     **兄弟元素**：具有相同父元素的元素，互为兄弟元素。     | <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240314022840148.png" alt="image-20240314022840148" style="width: 50%; display: block; margin: 0 auto;"  /> |

- 父元素也算是祖先元素的一种，但是一般还是称呼为父元素
- 子元素也算是后代元素的一种，但是一般还是称呼为子元素

### 后代选择器（day4|71p）

1. **后代选择器**：`selector_1 selector_2 ... selector_n`，选中指定元素中符合要求的**后代元素**。

2. **语法**

   ```css
   selector_1 selector_2 ... selector_n {
       属性名1: 属性值1;
       属性名2: 属性值2;
       ...
       属性名n: 属性值n;
   }
   ```

3. 注意

   - 这里的空格，语义上可以理解为“xxx中的”，即**后代**
   -  `selector` 既可以是**基本选择器**，也可以是**交并集选择器**
   - 后代选择器最终选择的是**后代**，**儿子、孙子、重孙子**等都是后代
   - HTML 结构一定要符合 HTML 的嵌套要求，例如不能在 `p` 标签中写 `h1`~`h6`（此时后代选择器 `p h1` 是不生效的）

### 子代选择器

1. **子代选择器**：`selector_1>selector_2>...>selector_n`，选中指定元素中符合要求的**子元素**。

2. **语法**

   ```css
   selector_1>selector_2>...>selector_n {
       属性名1: 属性值1;
       属性名2: 属性值2;
       ...
       属性名n: 属性值n;
   }
   ```

3. 注意

   - 子代选择器最终选择的是**子代**

   - 后代包含子代，范围更广

     <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240314104243620.png" alt="image-20240314104243620" style="width: 50%; display: block; margin: 0 auto;" />

### 兄弟选择器

1. **相邻兄弟选择器**：`selector_1+selector_2`，选中指定元素中符合要求的**相邻兄弟元素**。这里的**相邻**，指的是**紧挨着指定元素的下一个元素**。

2. **通用兄弟选择器**：`selector_1~selector_2`，选中指定元素中符合要求的**所有兄弟元素**。这里的**所有兄弟元素**，指的是**紧挨着指定元素下的所有元素**。

3. **语法**

   ```css
   selector_1+selector_2 {
       属性名1: 属性值1;
       属性名2: 属性值2;
       ...
       属性名n: 属性值n;
   }
   
   selector_1~selector_2 {
       属性名1: 属性值1;
       属性名2: 属性值2;
       ...
       属性名n: 属性值n;   
   }
   ```

4. 注意：两种兄弟选择器，选择的都是其**下边**的兄弟元素。

### 属性选择器

1. **属性选择器**

   - `[属性名]` 选中**具有某个属性**的元素
   - `[属性名="值"]` 选中**具有某个属性**，并且**属性值等于指定值**的元素
   - `[属性名^="值"]` 选中**具有某个属性**，并且**属性值以指定值开头**的元素
   - `[属性名$="值"]` 选中**具有某个属性**，并且**属性值以指定值结尾**的元素
   - `[属性名*="值"]` 选中**具有某个属性**，并且**属性值包含指定值**的元素

2. **语法**

   ```css
   [属性名] {
       属性名1: 属性值1;
       属性名2: 属性值2;
       ...
       属性名n: 属性值n; 
   }
   
   [属性名="值"] {
       属性名1: 属性值1;
       属性名2: 属性值2;
       ...
       属性名n: 属性值n; 
   }
   
   [属性名^="值"] {
       属性名1: 属性值1;
       属性名2: 属性值2;
       ...
       属性名n: 属性值n; 
   }
   
   [属性名$="值"] {
       属性名1: 属性值1;
       属性名2: 属性值2;
       ...
       属性名n: 属性值n; 
   }
   
   [属性名*="值"] {
       属性名1: 属性值1;
       属性名2: 属性值2;
       ...
       属性名n: 属性值n; 
   }
   ```
   
### 伪类选择器

1. **伪类**：像类，但不是类，是**元素特殊状态**的一种描述。
2. **伪类选择器**：选中某种特殊状态的元素。　

#### 动态伪类

|     伪类选择器     |                  含义                  |
| :----------------: | :------------------------------------: |
|  `selector:link`   | 标签（一般是超链接）**未被访问**的状态 |
| `selector:visited` |  标签（一般是超链接）**访问过**的状态  |
|  `selector:hover`  |       鼠标**悬停**在标签上的状态       |
| `selector:active`  | 标签**激活**（即按下鼠标不松开）的状态 |
|  `selector:focus`  |         标签**获取焦点**的状态         |

- 前四个伪类选择器，务必遵循 LVHA 的顺序编写样式表，即：`link`、`visited`、`hover`、`active`

  > LVHA 原因分析，以超链接 `a` 为例
  >
  > - 如果不触碰超链接，则处于 `link`/`visited` 状态
  > - 如果鼠标悬停在超链接上，则处于 `link`/`visited` 和 `hover` 状态
  > - 如果鼠标点击超链接不松开，则处于 `link`/`visited` 和 `hover` 和 `active`状态
  > - 基于上述分析，我们在使用伪类选择器时，最好遵循 LVHA 的顺序

- 只有表单元素才能使用 `:focus` 伪类，当点击元素、触摸元素、`tab` 键选择等方式都可以让元素获取焦点

#### 结构伪类（常用）

|        伪类选择器         |                             含义                             |
| :-----------------------: | :----------------------------------------------------------: |
|  `selector:first-child`   |    `selector` 选中的标签中是**其父亲的第一个儿子**的标签     |
|   `selector:last-child`   |   `selector` 选中的标签中是**其父亲的最后一个儿子**的标签    |
|  `selector:nth-child(n)`  |     `selector` 选中的标签中是**其父亲的第n个儿子**的标签     |
| `selector:first-of-type`  | `selector` 选中的标签中是**其父亲的第一个特定类型（同类型）儿子**的标签 |
|  `selector:last-of-type`  | `selector` 选中的标签中是**其父亲的最后一个特定类型（同类型）儿子**的标签 |
| `selector:nth-of-type(n)` | `selector` 选中的标签中是**其父亲的第n个特定类型（同类型）儿子**的标签 |

- 【HARD-TO-COMPREHEND】前三种伪类选择器的次序是在**所有兄弟元素中**的，后三种伪类选择器的次序是在**所有同类型兄弟元素中**的；这两类伪类选择器的不同是，比较的范围不同

- n 的不同取值对应不同的情况（括号里的内容的标准写法伪 `an+b`）

  |     n=?     |          含义          |
  | :---------: | :--------------------: |
  |  0 或不写   |      什么都选不中      |
  |      n      |     选中所有子元素     |
  | 1~$+\infty$ |  选中对应序号的子元素  |
  | 2n 或 even  | 选中序号为偶数的子元素 |
  | 2n+1 或 odd | 选中序号为奇数的子元素 |
  |    -n+3     |    选中前三个子元素    |

- 通过代码及其渲染结果举例

  ```html
  <!-- 网页结构：这一部分是不变的，然后我们根据不同的 CSS 观察网页的效果变化 -->
  <div>
      <span>选择器举例</span>
      <ul>
          <li>伪类选择器</li>
          <li>动态伪类</li>
          <li>结构伪类</li>
          <li>否定伪类</li>
          <li>UI伪类</li>
          <li>目标伪类</li>
          <li>语言伪类</li>
      </ul>
      <ul>
          <li>复合选择器</li>
          <li>并集选择器</li>
          <li>交集选择器</li>
          <li>属性选择器</li>
          <li>子代选择器</li>
          <li>后代选择器</li>
          <li>兄弟选择器</li>
      </ul>
  </div>
  ```

  |                             CSS                              |                             效果                             |                             解释                             |
  | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
  |                              无                              | <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240314170203671.png" alt="image-20240314170203671" style="width: 100%; display: block; margin: 0 auto;" /> |                      没有样式时候的网页                      |
  | <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240314170524726.png" alt="image-20240314170524726" style="width: 100%; display: block; margin: 0 auto;" /> | <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240314170203671.png" alt="image-20240314170203671" style="width: 100%; display: block; margin: 0 auto;" /> | `div ul` 选中 `div` 的后代元素 `ul`，此时可以找到两个 `ul` 元素；<br />`:first-child` 要求从这两个 `ul` 元素中找到是其父元素的第一个子元素，因为其父元素 `div` 的第一个子元素是 `span`，因此无法找到符合要求的 `ul`；<br />最终没有选中任何元素 |
  | <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240314171025777.png" alt="image-20240314171025777" style="width: 100%; display: block; margin: 0 auto;" /> | <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240314171034145.png" alt="image-20240314171034145" style="width: 100%; display: block; margin: 0 auto;" /> | `div ul` 选中 `div` 的后代元素 `ul`，此时可以找到两个 `ul` 元素；<br />`:last-child` 要求从这两个 `ul` 元素中找到是其父元素的最后一个子元素，因为其父元素 `div` 的最后一个子元素是 `ul`，因此可以找到符合要求的 `ul`；<br />最终选中了最后一个 `ul` 元素 |
  | <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240314171405546.png" alt="image-20240314171405546" style="width: 100%; display: block; margin: 0 auto;" /> | <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240314171416165.png" alt="image-20240314171416165" style="width: 100%; display: block; margin: 0 auto;" /> | `div ul` 选中 `div` 的后代元素 `ul`，此时可以找到两个 `ul` 元素；<br />`:nth-child(2)` 要求从这两个 `ul` 元素中找到是其父元素的第二个子元素，因为其父元素 `div` 的最后一个子元素是 `ul`，因此可以找到符合要求的 `ul`；<br />最终选中了第一个 `ul` 元素 |
  |                      以上三种伪类选择器                      |                        其次序都是基于                        |                  父元素里边的所有子元素排的                  |
  |                      以下三种伪类选择器                      |                        其次序都是基于                        |              父元素里边的所有同类型的子元素排的              |
  | <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240314172226190.png" alt="image-20240314172226190" style="width: 100%; display: block; margin: 0 auto;" /> | <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240314172241338.png" alt="image-20240314172241338" style="zoom:50%;" /> | `div ul` 选中 `div` 的后代元素 `ul`，此时可以找到两个 `ul` 元素；<br />`:first-of-type` 要求从这两个 `ul` 元素中找到是其父元素的第一个 `ul` 子元素；<br />最终选中了第一个 `ul` 元素 |
  | <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240314172523529.png" alt="image-20240314172523529" style="width: 100%; display: block; margin: 0 auto;" /> | <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240314172534570.png" alt="image-20240314172534570" style="width: 100%; display: block; margin: 0 auto;" /> |                         原因显而易见                         |
  | <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240314172640457.png" alt="image-20240314172640457" style="width: 100%; display: block; margin: 0 auto;" /> | <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240314172534570.png" alt="image-20240314172534570" style="width: 100%; display: block; margin: 0 auto;" /> |                         原因显而易见                         |

#### 结构伪类（不常用）

|           伪类选择器           |                             含义                             |
| :----------------------------: | :----------------------------------------------------------: |
|  `selector:nth-last-child(n)`  |   `selector` 选中的标签中是**其父亲的倒数第n个儿子**的标签   |
| `selector:nth-last-of-type(n)` | `selector` 选中的标签中是**其父亲的倒数第n个特定类型（同类型）的儿子**的标签 |
|     `selector:only-child`      |          `selector` 选中的标签中**没有兄弟**的元素           |
|    `selector:only-of-type`     | `selector` 选中的标签中**没有特定类型（同类型）兄弟**的元素  |
|            `:root`             |                            根元素                            |
|        `selector:empty`        | `selector` 选中的标签中**内容为空**的元素（注意空格也算内容） |

#### 其他伪类

| 伪类     |      形式      |                       含义                       |
| -------- | :------------: | :----------------------------------------------: |
| 否定伪类 | `:not(选择器)` |           表示**排除括号中条件**的元素           |
| UI伪类   |   `:checked`   |         表示**被选中的复选框或单选按钮**         |
|          |   `:enabled`   | 表示**可用的表单元素**（即么有 `disabled` 属性） |
|          |  `:disabled`   | 表示**不可用的表单元素**（即有 `disabled` 属性） |
| 目标伪类 |   `:target`    |              选中**锚点指向**的元素              |
| 语言伪类 |   `:lang()`    |            根据**指定的语言**选择元素            |

### 伪元素选择器

1. **伪元素**：很像元素，但不是元素，是元素中的一些**特殊位置**。
2. **伪元素选择器**：可以选中元素中的一些特殊位置。
   - 伪类以 `:` 开始，伪元素以 `::` 开始

|      伪元素      |                             含义                             |
| :--------------: | :----------------------------------------------------------: |
| `::first-letter` |                   选中元素的**第一个文字**                   |
|  `::first-line`  |                     选中元素的**第一行**                     |
|  `::selection`   |                   选中**被鼠标选中**的内容                   |
| `::placeholder`  |                   选中输入框的**提示文字**                   |
|    `::before`    | 在**元素最开始的位置**，创建一个子元素（用 `content` 指定内容） |
|    `::after`     | 在**元素最后的位置**，创建一个子元素（用 `content` 指定内容） |

## SUMMARY of SELECTORS

<img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/%E9%80%89%E6%8B%A9%E5%99%A8.svg" alt="选择器" style="width: 85%; display: block; margin: 0 auto;" />

 ## 选择器优先级

1. **样式冲突**：当通过**不同选择器**，选中**相同的元素**，并且为**相同的样式名**设置**不同的值**时，就发生了样式冲突，此时就需要根据**选择器的优先级**决定到底应用哪个样式。其中，当两个选择器优先级相同时，则遵从“**后来居上**”的原则，应用位于较下边的样式。

2. 简单的说，有以下优先级：**!important>行内样式>ID选择器>类选择器>元素选择器>通配选择器>继承的样式**。

   - 其中 `!important` 是写在一个**声明之后，分号之前**，表明该声明最重要

     ```css
     .slogan{
         color: purple !important;
     }
     ```

   - **继承的样式**指的是，任何标签会默认继承其祖先元素的样式

3. 对于复杂的复合选择器，我们采用①**计算权重**，②**依次比较**的方式进行优先级比较。

   - **权重的计算**：`(a,b,c)`，a 是 ID 选择器个数，b 是类、伪类、属性选择器个数，c 是元素、伪元素选择器个数

     <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240314220844059.png" alt="image-20240314220844059" style="width: 45%; display: block; margin: 0 auto;" />

   - **优先级比较**：按照**从左到右**的顺序，依次比较大小，当前位胜出后，后面的不再对比（如 (1,0,0)>(0,2,2), (1,1,0)>(1,0,3)）

4. 权重计算举例

   <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240314221211311.png" alt="image-20240314221211311" style="width: 85%; display: block; margin: 0 auto;" />

 ## 三大特性

1. **层叠性**：如果发生了样式冲突，那就会根据一定的规则（选择器的优先级），进行样式的层叠（覆盖）。
2. **继承性**：元素会自动拥有其父元素或其祖先元素上所设置的某些样式。
   - 优先级继承**离得近**的祖先元素的某些样式
   - 有些属性是可以继承的，有些属性是不可以继承的
   - 常见的可继承属性有：`text-??`, `font-??`, `line-??`, `color`, ...
3. **优先级**：简单的说，!important>行内样式>ID选择器>类选择器>元素选择器>通配选择器>继承的样式；复杂的复合选择器则需要通过权重计算进行优先级比较。
   - **并集选择器的每一个部分的权重都是分开计算的**

## 像素和颜色（day5|88p）

1. **像素**（pixel）：图像中的最小的元素点，具有特定的位置及颜色值，每个像素的颜色是由强度不同的红、绿、蓝三原色组合而成的。

   > 光的三原色：红、绿、蓝
   >
   > 颜料的三原色：红、黄、蓝

2. **颜色**的表示

   - **颜色名**：使用颜色对应的**英文单词**表示颜色，如 red、green、blue、purple 等

     ```css
     color: red;
     ```

     - 这种颜色表达方式比较单一，使用并不多
     - 具体颜色名需要参考 MDN 官方文档，不能胡写

   - rgb/rgba：使用**红、绿、蓝**这三种光的三原色进行组合来表示具体颜色，其中 r 表示红色，g 表示绿色，b 表示蓝色，a 表示透明度

     ```css
     color: rgb(255, 0, 0); /* 红色 */
     color: rgb(0, 255, 0); /* 绿色 */
     color: rgb(0, 0, 255); /* 蓝色 */
     color: rgb(0, 0, 0); /* 黑色 */
     color: rgb(255, 255, 255); /* 白色 */
     
     color: rgb(100%, 0%, 0%); /* 红色 */
     
     color: rgba(255, 0, 0, 0.5); /* 半透明的红色 */
     color: rgba(100%, 0%, 0%, 50%); /* 半透明的红色 *
     ```

     - 若 r=g=b，则呈现是灰色，三者取值越大，则灰色越浅
     - `rgb(0,0,0)` 是黑色，`rgb(255,255,255)` 是白色
     - rgb 可以用 0~255 的数字表示，也可以用 0%~100% 的百分比表示，一定要统一使用 
     - a 可以用 0~1 的数字表示，也可以用 0%~100% 的百分比表示

   - HEX/HEXA：原理同 rgb/rgba，不过是使用**十六进制**，用六个数字表示一个特定颜色，两个数字为一组，三组分别对应红、绿、蓝三原色

     ```css
     color: #ff0000; /* 红色 */
     color: #00ff00; /* 绿色 */
     color: #0000ff; /* 蓝色 */
     
     color: #ff9988; /* 可简写为 #f98 */
     color: #ff998866; /* 可简写为 #f986 */
     ```

     - IE 浏览器不支持 HEXA，但支持 HEX
     - 如果要引入透明度，则使用八个数字表示一个颜色，两个数字为一组，每组取值范围为 00~ff
     - 如果每组的两个数字相同，则可以进行简写，每组用一个数字表示颜色，取值范围为 0~f，如 ffaa99 可简写为 fa9，ffaa8811 可简写为 fa81

   - HSL/HSLA：使用**色相、饱和度、亮度**三者进行组合来表示具体颜色，其中 H 表示色相环上的角度，S 表示饱和度，L 表示亮度，a 表示透明度

     ```css
     color: hsl(0, 100%, 50%); /* 红色 */
     color: hsla(0, 100%, 50%, 50%); /* 半透明红色 */
     ```

     - 色相：取值范围是 0~360 度，具体每个度数对应的颜色如下色相图

       <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240315122329918.png" alt="image-20240315122329918" style="width: 40%; display: block; margin: 0 auto;" />

     - 饱和度：取值范围是 0%~100%

     - 亮度：取值范围是 0%~100%

## 常用字体属性

1. 字体**大小** `font-size`
   - 每个浏览器都会有**默认字体大小**和**最小支持字体大小**，且都是可以在浏览器设置页面更改的，例如，Chrome 默认最小支持文字大小为 12px，默认字体大小为 16px
   - 如果给标签设置的字体大小<浏览器最小支持字体大小，则浏览器只显示其最小支持的字体大小
   - 可以通过给 `body` 设置 `font-size` 属性，从而控制整个页面的默认字体大小（CSS 的三大特性之继承性）
   - 注：通过开发者工具的 styles 选项卡，可以看到所选元素的样式和继承样式等信息
2. 字体**族** `font-family`
   - 字体可以分为**衬线字体**（serif）和**非衬线字体**（sans-serif），实际开发中多使用非衬线字体
   - 设置标签的字体时，最好使用字体的**英文**名称，并且用**双引号**包裹，多字体之间用**逗号**隔开
   - 给标签设置多个字体时，浏览器会按照**从左到右**的顺序逐个查找，系统中找到对应字体则使用，否则往后继续查找
   - 给标签设置多个字体时，通常以（不带双引号）serif 或 sans-serif 结尾，代表一类字体，意思是：如果浏览器没有找到前边的字体，则**从系统中的衬线/非衬线字体中找一个字体**渲染网页
   - windows 系统中的**默认字体**是**微软雅黑**
3. 字体**风格** `font-style`（可取值：`normal`、`italic`、`oblique`）
   - `normal` 是默认值，表示**正常**；`italic` 是斜体，特指**字体自带**的斜体效果；`oblique` 是斜体，表示**强制倾斜**得到的斜体效果
   - 开发中推荐使用 `italic` 实现斜体效果，浏览器会先去找改字体库是否存在相关文字的斜体，如果存在则使用，否则将将相关文字强制倾斜来实现斜体效果
4. 字体**粗细** `font-weight`（可取值：`lighter`、`normal`、`bold`、`bolder`、100~1000）
   - `normal` 是默认值，表示**正常**；`lighter` 表示**细**；`bold` 表示粗；`bolder` 表示**很粗**
   - 100~1000 的取值是无单位的，**数值越大则字体越粗**（也有可能一样粗）；100~300 等同于 `lighter`、400~500 等同于 `normal`、600 及以上等同于 `bold`
   - 与字体风格类似，如果字体设计的过程中只设计了三种粗细，则无论怎么调整，最终只能渲染出三种字体的粗细效果（例如 `bold` 和 `bolder` 的效果是相同的，100 和 300 的效果是相同的）
5. 字体的**复合属性** `font`
   - 字体的复合属性即将字体**大小、族、风格、粗细**合并成一个属性
   - 字体的复合属性要求
     - 必须写上**字体大小、字体族**
     - **字体族必须是最后一位、字体大小必须是倒数第二位**
     - 字体风格与字体粗细则是可选的，可以不写，写了也没有顺序要求
     - 各个属性之间使用**空格**分开

```css
div {
    font-size: 40px;
    font-family: "STCaiyun", "Microsoft YaHei", sans-serif;
    font-style: italic;
    font-weight: bold;
}

h2 {
    font: bold italic 100px "STCaiyun", "Microsoft YaHei", sans-serif;
}
```

## 从字体设计角度讨论 font-size

1. 设计师怎么设计字体（简单说）？每个字体都是放在一个**字体设计框**中进行设计的；其中 X 最为特殊，其底部与字体设计框的**基线**重合。

   <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240315170606134.png" alt="image-20240315170606134" style="width: 60%; display: block; margin: 0 auto;" />

   <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240315170847900.png" alt="image-20240315170847900" style="width: 60%; display: block; margin: 0 auto;" />

2. `font-size` 是什么？`font-size` 可以理解为**字体设计框的高度**，当我们调整 `font-size` 时，其实是调整字体设计框的高度，与之同时，字体设计框的宽度也等比例变化，字体于是也被放大了。

3. 重要结论

   - 由于字体设计原因，**文字最终呈现的大小，并不一定与 `font-size` 的值一致**，可能大，也可能小
   - 通常情况下，文字相对字体设计框，并不是垂直居中的，**通常**都**靠下**一些。

## 常用文本属性

1. 文本**颜色** `color`（可选值：颜色名、rgb/rgba、HEX/HEXA、HSL/HSLA）
2. 文本**间距**
   - **字母间距** `letter-spacing`（单位是 px）
   - **单词间距** `word-spacing`（单位是 px）
   - 注
     - 浏览器通过**空格**识别单词
     - 正值让间距增大，负值让间距缩小
3. 文本**修饰** `text-decoration`（可选值：`none`、`underline`、`overline`、`line-through`；可搭配 `dotted`、`wavy` 和颜色使用）
   - `none` 表示无装饰线；`underline` 表示下划线；`overline` 表示上划线；`line-through` 表示删除线
   - `dotted` 表示虚线；`wavy` 表示波浪线
   - 属性值举例：每种**线**都可以指定其**线型**和颜色等样式
     - `overline dotted green`：绿色上划虚线
     - `underline wavy red`：红色下划波浪线
     - `line-through`：删除线
     - `none`：无任何线（可用于删除超链接 `a` 标签的下划线）
4. 文本**缩进**：`text-indent`（单位是 px）
   - `text-indent` 取值一般是 `font-size` 的两倍，可以实现缩进两个文字的效果
5. 文本**水平对齐** `text-align`（可选值：`left`、`right`、`center`）
   - `left` 是默认值，表示左对齐；`right` 表示右对齐；`center` 表示居中对齐
6. 文本**行高** `line-height`（可选值：`normal`、具体的像素、数字、百分比）
   - `normal` 表示浏览器根据文字大小决定的一个默认值；具体的像素表示：直接设置行高（px）；数字表示：设置行高为**文字大小（`font-size`）的倍数**；百分比表示：设置行高为**文字大小的百分比**
   - 行与行之间是**紧紧贴**在一起的
   - 最好**不要让行高等于字体大小**（`line-height==font-size`）！由于字体设计的过程中，有些文字可能会超出字体设计框，因此如果行高等于字体大小，则可能会发生“字体打架”的情况
   - 由于字体设计的原因，文字在一行中并不是绝对垂直居中
7. 文本**垂直对齐**（暂时用行高办法实现）
   - 置顶：默认情况就是顶部对齐，不做讨论
   - 居中：对于单行文字，让 `height` 等于 `line-height`
   - 底部：对于单行文字，让 `height × 2 - font-size -x` 等于 `line-height`，其中 `x` 是根据特定的字体，动态确定的一个值
   - 注：垂直方向上的对齐，下面会用**定位**的方式去实现

## 进一步讨论 line-height

1. 关于行高的三点讨论

   - `line-height` **过小**会怎样？

     <img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240315172048104.png" alt="image-20240315172048104" style="width: 60%; display: block; margin: 0 auto;" />

     - 文字重叠
     - 同时行高最小值是 0，不能是负数

   - `line-height` 的**继承性**

     - 行高是**可继承**的属性
     - 为了更好的呈现文字，**最好让行高等于一个数值（文字大小的倍数）**，这样的话，虽然子代元素的行高与祖先元素的行高相同，但是子代元素会根据其文字大小（`font-size`）来计算自己的行高

   - `line-height` 和 `height` 之间的关系

     - 如果已经设置了 `height`，则高度就是 `height`
     - 如果没有设置 `height`，则高度就是 `line-height`

2. 行高的应用场景

   - 调整**多行文字行与行的间距**
   - **单行**文字的**垂直居中**：让 `height` 等于 `line-height`

## 元素垂直对齐 vertical-align

`vertical-align`，可选值：`baseline`、`top`、`middle`、`bottom`，用于指定①**同一行元素之间**或②表格**单元格内文字**的垂直对齐方式。

- `baseline` 默认值，表示使**元素的基线**与**其父元素的基线**对齐
- `top` 表示使元素的**顶部**与其所在行的**顶部**对齐
- `bottom` 表示使元素的**底部**与其所在行的**底部**对齐
- `middle` 表示使元素的**中部**与父元素的**基线加上父元素字母 x 的一半**对齐

<img src="https://cdn.jsdelivr.net/gh/Nasir1423/blog-img@main/image-20240315173722402.png" alt="image-20240315173722402" style="width: 60%; display: block; margin: 0 auto;" />

## 列表相关属性

## 边框相关属性

## 表格独有属性

## 背景相关属性

## 鼠标相关属性

## 常用长度单位

## 元素的显示模式

## 盒子模型
