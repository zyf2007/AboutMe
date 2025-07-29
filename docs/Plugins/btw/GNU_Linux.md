# GNU/Linux

<html>
<head>
    <style>
        .arch-banner {
            width: 100%;
            background-color: #333333;
            border-radius: 8px;
            padding: 16px;
            display: flex;
            align-items: center;
            font-family: Arial, sans-serif;
        }
        
        .arch-text {
            color: white;
            font-size: 14px;
        }

        .btw-text {
            color: #3392CE;
            font-size: 30px;
            margin-right: 8px;
            font-weight: bold;
        }
        .arch-logo {
            width: 8rem;
            margin-right: 8px;
        }
    </style>
</head>
<body>
    <div class="arch-banner">
        <span class="arch-text">进来啥都别说，先一起喊：</span>
        <span class="btw-text">BTW I use</span>
        <img 
            src="https://www.archlinuxcn.org/wp-content/themes/askin2010/archlogo.8a05bc7f6cd1.svg" 
            alt="Arch Linux Logo" 
            class="arch-logo"
        />
        <span class="arch-text"></span>
    </div>
</body>
</html>

> ## 如果你不知道标题是什么意思：
> [什么是Linux？](https://www.runoob.com/linux/linux-intro.html)

---
## 我属于哪类 Linux 用户？
首先要声明的是，我们讨论的**不是**将操作系统作为玩具的Hyprland用户/平铺管理器用户。在Linux桌面领域，胡桃酱只是**用户**而不是开发者，所以本文中的所有内容都**没有**经过正确性的确认，仅凭借**个人理解**编写。  


下面展示我的配置：
{{ asciinema("https://114514.zroevn.cn/imgs/arch_neofetch.cast") }}
[Budgie](https://buddiesofbudgie.org)是我认为最**不折腾**的桌面环境。窗口管理器只拥有较少的用户设置项目，大部分默认设置都可以保留。 **我对我的桌面环境的 customize 仅包含配色主题，壁纸，dock 栏。**   
*暴论：那些折腾平铺式桌面管理器的都是日常只需要开一个浏览器、一个终端和一个即时通讯软件的用户。由于我的窗口管理需求较为复杂（尤其是Unity编辑器），我只能使用传统的窗口管理。*

<p style="color:#E34092;">下面的文章部分都包含一个前提：我们将操作系统视作一种工具，而不是玩具。Linux 桌面不是 Linux 服务器运维，我使用 Linux 桌面不代表我会使用各种网络安全工具和服务器配置工具。</p>
---

## ArchLinux 受到的误解
如果你在各种 SNS 上刷到过 Arch Linux 相关的推文或是视频，会发现这个distro往往被塑造成一个十分麻烦，十分折腾的系统。然而Arch实际上从安装到使用和维护都是一个十分**懒人向**的，**实用主义**的 distro。
#### 安装到底麻不麻烦？
一直以来，大家首先喜欢吐槽的就是Arch的安装程序——实际上桌面操作系统的安装无非就是那么**几个步骤***（分区，创建文件系统，写入文件，设置时区、本地化、网络、添加引导项，创建用户）*。  
造成这种「**错觉**」的原因就是：Wizard 类安装程序相当于将文档和用户选项进行了**一一对应**的展示，而 Archiso 则建议在**另一台**设备上**阅读文档**来进行安装。
#### 安装后的配置有多方便？
众所周知，**大部分**操作系统在安装后还需要进行大量的配置才能满足日常使用需求。实际上在开始添加自己的软件**之前**，Windows 就已经变得相当麻烦：
> 根据我的个人经验，Windows 11 全新安装后的步骤大概有：  
> 1. 改回经典右键菜单（需要查找资料完成）  
> 2. 禁用小组件等无用服务（减少打扰和广告）  
> 3. 将C盘中用户家目录的所有目录迁移到其他盘符  
> 4. 更新winget，安装和配置 PowerShell7，安装 scoop（方便管理软件）  
> 5. 激活  

即便如此，任务管理器仍然充斥着大量我们不认识的进程，可能需要随着对我们造成影响再逐个禁用服务。  
而这是全新安装的 ArchLinux 的`pstree`：
``` bash
❯ pstree
systemd─┬─NetworkManager──4*[{NetworkManager}]
        ├─dbus-broker-lau──dbus-broker
        ├─login──zsh──pstree
        ├─systemd──(sd-pam)
        ├─systemd-hostnam
        ├─systemd-journal
        ├─systemd-logind
        ├─systemd-timesyn──{systemd-timesyn}
        ├─systemd-udevd
        └─systemd-userdbd──3*[systemd-userwor]
```
一目了然，我们可以知道**所有**进程的作用，且全部都是**必要**进程，**不需要**做任何清理，可以直接开始在此基础上进行「创作」：直接开始安装自己需要的软件，主题，服务。并且在接下来的使用中，你可以确保 pstree 中的**所有**进程都是我们认识的——都是我们**亲自** start 或者 enable 的。**不可能无故出现自己不认识的进程和文件：这才是「电脑真正属于自己」的感觉。**
#### 滚动更新到底会不会挂？
说什么都没用，从2023年12月30日到现在我的系统总共滚挂过**0次**，在社区公告的提醒下手动介入过2次。*(我没有定期更新系统的习惯，只会在安装新的软件包前[阅读社区公告](https://archlinux.org/news/)并进行一次系统更新。)*

{{ asciinema("https://114514.zroevn.cn/imgs/arch_first_install_time.cast") }}

---

## 为什么我选择Linux作为主力系统？
对于这个问题，说实话我并**不想要**从“自由软件”等等十分高大上的哲学或者“隐私安全”等这些我们大陆用户根本不配拥有的权利这样的角度去编写一些看起来十分正确但又没有说服力的理由（个人观点）。作为每天都要在身边陪伴自己战斗的工具，**「好用」**一定是最为重要的特性。
### 在使用计算机时，我会在意什么？
* 操作系统不应该在我将计算机闲置（没有进行键鼠输入）的时候，在我**不知情**的情况下**创建进程**（或是突然使系统进程开始活跃），占用资源导致发热，噪音和能耗。
* 在命令行中启动，运行和奔溃应用程序时应当**输出有效的日志**。【方便 debug 和环境配置检查。】
* 非系统工具类应用程序（携带版应用程序除外）在运行时**不应该**有权限在用户的家目录以外的位置（例如软件的安装目录）创建和修改文件。【即使重新安装应用程序，乃至整个系统，用户的 config 都还是重装之前的样子；而当应用程序运行出现问题需要重置时，只需要删除它的 config 目录即可】
* 应用程序应该在需要管理员权限进行操作时**说明原因**并请求对于单个操作的**临时提权**，**不应该**直接以管理员身份运行。
* 用户应当能够通过系统目录的文件名反向查询到其属于哪个软件包。【将系统级目录抽象成一个一个的软件包，尽可能减少用户手动进行逐个文件的管理】
* 当系统出现错误时，用户可以通过对其中**某一部分**重新配置以进行修复。【完整的重装系统会需要**数以月计**的时间来恢复到自己曾经熟悉的环境】

#### 软件包管理
{{ asciinema("https://114514.zroevn.cn/imgs/paru_Syu.cast") }}
包管理方面我并不想要吹aur，因为 aur 和 scoop 的**都不缺软件包**。但Windows的软件管理策略仍然存在很多**不方便不合理**的地方：即使是使用了包管理器也是打开安装程序然后让安装程序自己处理软件的安装，有时还不能静默安装，需要弹出 UAC 手动授权并手动点击下一步安装，安装过程也非常不透明等等：

| **对比维度** | **Windows安装器** | **Linux包管理器** |
| -------- | -------- | -------- |
| **安装方式** | 单个 exe 或 msi 文件，需要手动点下一步，**天朝软件**还要避开各种自启动陷阱或捆绑安装。<br> （你根本不知道他会对你的系统做出什么修改‼️）（有些环境变量还要自己加） | 包管理器输入软件名称直接安装/更新，**无需**人工干预 <br> 包管理器只负责复制文件和运行hook，这也使得系统级目录有一个统一的管理器在管理，而不是安装器各管各的|
| **依赖管理** | 依赖关系需安装器自行处理，部分场景还要去微软官网自己找（如VC++运行库、.NET框架）。 | 包管理器自动解析并安装依赖 |
| **更新机制** | 软件自己检查更新，然后自己更新自己 | 包管理器统一更新 |

不知道安装器和卸载器会对系统做出什么样的修改这一点，其实最大的问题不在于安全性（对我来说），而是在于**出了问题不方便修复**，容易增加很多不必要的**系统重装**——*一些软件安装上之后，卸载掉，就**再也**安装不上了，你也**无法**把系统恢复到原状 因为你不知道安装器对你的系统做出了什么修改；而linux可以很轻松的让一款软件的所有痕迹**完全消失**，在包管理器和用户 config 目录的帮助下*  
久而久之，经过各种软件的安装，卸载，再安装不同的版本这样的流程下来，Windows就会变得**越来越乱**，不知道系统里存了多久之前的**历史遗留文件**；而 Linux 包管理器则可以做到**逻辑上**的「**装多少删多少**」，系统几乎一直和新的一样。  
补充：最近因为学习嵌入式开发而有在使用 Windows ，还发现某些软件下载之前还需要在官网上注册登录，填写个人信息，订阅邮件广告，然后才能把 exe 安装包的下载链接给我（安装时还是要选一遍同意协议）。**这是我近几年来在装软件这件事上消耗时间最长的一次（部分 Windows 商业软件并不能收入包管理器中）**。

#### 配置文件管理
在Linux下，`~/.config`等文件夹包含了**所有**的用户级配置文件——也称为 dotfile。可以说，dotfile就是你对应用程序进行的**所有**设置：当你需要迁移系统时（例如更换了计算机或重新安装了系统），只需要迁移你的`~/`和`/etc`中修改过的配置文件，就可以把**一切**都恢复到原本的样子（包括桌面环境的控件布局，各种包管理器的镜像源，neovim 插件等等）
{{ asciinema("https://114514.zroevn.cn/imgs/ls_config.cast") }}
 
实际上由于我们可以轻松的了解到 Linux 运行细节，所以我们可以在系统损坏时针对损坏的部分进行重装和修复（例如桌面环境，grub 引导），而不用重装整个系统。所以几乎遇不到“重新安装了系统”的情况。  
（Windows下我无法迁移`Local`,`LocalLow`,`Roaming`,`ProgramData`，甚至无法看懂这些目录下的部分文件来源）
#### 零打扰
在**科技巨头**的控制下，你的系统可以**随时**被插入他们想要的信息，或随时打扰你的工作。
>  Windows 11 测试版中，**广告**出现在**资源管理器**中。Windows 10 也曾在**开始菜单**里出现过类似系统更新推送的广告选项，点击后会打开京东购物页面，其资源管理器里还有 OneDrive 云存储的广告，锁屏界面、Edge 浏览器、任务栏上也**都曾有过广告**。  
> 由于 Windows 10 将于 2025 年 10 月 14 日结束支持，微软为促使用户升级到 Windows 11，在 Windows 10 也曾弹出过**全屏**更新广告——用户若想拒绝升级，需找到并点击**屏幕底部**的 “保留 Windows 10” 链接，但点击后**不会**直接返回桌面，而是会依次打开 “介绍 Windows 11” 等页面**继续推广**，通常需**五步操作**才能最终关闭。


ArchLinux的维护策略使得整个系统的不同部分完全由不同的组织开发和维护——完全不可能被某个组织控制。就连系统更新需要手动干预也只能通过在[官网](https://archlinux.org/)发布通知的形式告诉用户。

#### 后台服务
最近(2025.7)我购买了一台新的游戏本，预装了家庭版 Windows11 。经过我短暂的使用，（为了避免自动运行搜索索引，已经禁用了 Windows Search 服务）而目前还是遇到了一些**高占用**的后台服务，例如“ Microsoft 恶意软件删除程序”。并不是觉得这类服务不应该存在（其实用处应该不大吧？），但是当我几分钟没有对电脑进行输入操作的时候，这类进程就会**将单个 CPU 核心拉满**到 100% 的占用，导致游戏本产生**超大的噪音**，多少会对我本人或大家造成一定的**打扰**。然而在我实际使用下，ArchLinux 不仅可以在闲置的时候实现 0% 的 CPU 占用，即使是系统更新时安装 DKMS 内核模块也**不会**造成如此大的噪音。  


经过近期的实际使用，我发现 Windows 会在闲置时产生更大的噪音，而Linux在开着一个30多个网页的浏览器，两个VSCode,十多个终端的情况下，闲置一段时间（不熄屏）可能会直接让风扇关闭，同时只会产生超低的功耗。

## 我现在的启动项配置
即使ArchLinux更适合作为主力系统，Windows也有自己不可替代的优势：游戏多。目前我的配置是由grub引导，ArchLinux作为第一启动项，Windows作为第三启动项——Windows进入系统登录后会自动启动Steam大屏幕模式（把Windows作为游戏主机使用）。如果在Windows启动前打开电视，Steam大屏幕模式将会自动在电视上启动，方便直接用游戏手柄控制电脑。

在前文中也有提到，ArchLinux 在系统出现问题时**不需要**重装整个系统，可以使用 Live 系统中进行修复。而 Archiso LiveUSB 系统与正常安装的 ArchLinux 在进行系统修复方面的一个主要的区别就是拥有`pacstrap`和`arch-chroot`这类安装工具 scripts 。而这些 scripts 刚好属于一个软件包：`arch-install-scripts`。因此，我只需要在我的硬盘上创建一个较小的分区，然后安装一个只包含基础系统和`arch-install-scripts`软件包的 ArchLinux 就可以无需u盘也能轻松进行系统调试和修复了。  
（实际上安装这个备用系统的过程本身也**不需要**使用u盘，下面是我使用主力系统在**同一块硬盘的其他分区**上安装备用系统的全过程：
```bash
sudo cfdisk /dev/nvme0n1
sudo mkfs.ext4 /dev/nvme1n1p8
sudo mount /dev/nvme0n1p8 /mnt
sudo pacstrap /mnt linux linux-firmware networkmanager sudo zsh base
sudo genfstab -U /mnt > /mnt/etc/fstab
```
至此，**新系统已经安装完毕**，接下来到系统内部进行时区，设备名，用户等基础配置:
```bash
# 设置设备名
echo 设备名 > /etc/hostname
echo 127.0.0.1 localhost > /etc/hosts
echo ::1 localhost >> /etc/hosts
echo 127.0.0.1 设备名.localdomain 设备名 >> /etc/hosts

ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime # 设置时区
vim /etc/locale.gen # 添加 en_US.UTF-8 UTF-8 和 zh_CN.UTF-8 UTF-8
locale-gen
echo 'LANG=en_US.UTF-8'  > /etc/locale.conf

# 创建用户
useradd -m -G wheel -s /bin/bash 用户名
passwd 用户名 # 设置密码
```
至此，新系统基础信息已经设置完毕，只需要将新系统添加到启动菜单就可以重启进入系统啦！
```bash
exit
grub-mkconfig -o /boot/grub/grub.cfg
```
![我的Grub页面](https://raw.gitcode.com/hutao_zyf/blog_assets/raw/main/imgs/5345490099fdfd1a9c2662b35fe52167.jpg)
---

## 如果你也想试试ArchLinux？
Arch拥有桌面distro中最活跃的社区和最完整的文档，它们可以帮你解决入坑使用遇到的全部问题：  

* [阅读文档](https://wiki.archlinuxcn.org/wiki/%E9%A6%96%E9%A1%B5)  
* [访问社区](https://bbs.archlinux.org)





