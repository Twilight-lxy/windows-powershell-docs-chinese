---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
Download Help Link: https://aka.ms/winsvr-2025-pshelp
Help Version: 5.0.0.1
Locale: en-US
Module Guid: d57aee1e-6fe7-4bbc-8c57-8675a3a83e0d
Module Name: BranchCache
ms.date: 12/20/2016
title: BranchCache
---

# BranchCache模块
## 说明
此参考资料提供了所有与BranchCache管理功能相关的cmdlet的描述和语法信息。这些cmdlet按照命令开头所使用的动词（即动词部分）的字母顺序进行排列。

## BranchCacheCmdlets
### [Add-BCDataCacheExtension](./Add-BCDataCacheExtension.md)
通过添加一个新的缓存文件，增加托管缓存服务器上可用的缓存存储空间。

### [Clear-BCCache](./Clear-BCCache.md)
删除所有数据缓存文件和所有哈希缓存文件中的所有数据。

### [Disable-BC](./Disable-BC.md)
禁用BranchCache服务。

### [禁用 BC 下降级功能](./ Disable-BCDowngrading.md)
禁止降级功能，从而防止客户端计算机向内容服务器请求旧版本的内容信息。

### [禁用在电池供电时运行BCServe](./Disable-BCServeOnBattery.md)
配置客户端在仅使用电池供电的情况下，在分布式缓存模式下忽略内容发现请求。

### [Enable-BCDistributed](./Enable-BCDistributed.md)
启用BranchCache功能，并配置计算机以分布式缓存模式运行。

### [Enable-BCDowngrading](./Enable-BCDowngrading.md)
用于指示运行在降级模式下的操作系统的客户端计算机执行相应操作。

### [Enable-BCHostedClient](./Enable-BCHostedClient.md)
将 BranchCache 配置为以托管缓存客户端模式运行。

### [Enable-BCHostedServer](./Enable-BCHostedServer.md)
将 BranchCache 配置为以托管缓存服务器模式运行。

### [Enable-BCLocal](./Enable-BCLocal.md)
以本地缓存模式启用BranchCache服务。

### [Enable-BCServeOnBattery](./Enable-BCServeOnBattery.md)
配置客户端在仅使用电池供电的情况下，以分布式缓存模式监听内容发现请求。

### [Export-BCCachePackage](./Export-BCCachePackage.md)
导出一个缓存包。

### [Export-BCSecretKey](./Export-BCSecretKey.md)
将一个密钥导出到一个文件中。

### [Get-BCClientConfiguration](./Get-BCClientConfiguration.md)
检索当前的BranchCache客户端计算机设置。

### [Get-BCContentServerConfiguration](./Get-BCContentServerConfiguration.md)
检索当前的BranchCache内容服务器设置。

### [Get-BCDataCache](./Get-BCDataCache.md)
检索一个表示BranchCache数据缓存的对象。

### [Get-BCDataCacheExtension](./Get-BCDataCacheExtension.md)
从托管的缓存服务器中检索表示BranchCache数据缓存扩展的对象。

### [Get-BCHashCache](./Get-BCHashCache.md)
检索 BranchCache 的哈希缓存数据。

### [Get-BCHostedCacheServerConfiguration](./Get-BCHostedCacheServerConfiguration.md)
获取当前BranchCache托管缓存服务器的设置信息。

### [Get-BCNetworkConfiguration](./Get-BCNetworkConfiguration.md)
检索当前的BranchCache网络设置。

### [Get-BCStatus](./Get-BCStatus.md)
检索一组对象，这些对象提供BranchCache的状态和配置信息。

### [Import-BCCachePackage](./Import-BCCachePackage.md)
导入一个缓存包。

### [Import-BCSecretKey](./Import-BCSecretKey.md)
导入BranchCache用于生成分段密钥（segment secrets）所需的加密密钥。

### [Publish-BCFileContent](./Publish-BCFileContent.md)
为共享文件夹中的文件生成哈希值。

### [Publish-BCWebContent](./Publish-BCWebContent.md)
为网页内容生成哈希值。

### [Remove-BCDataCacheExtension](./Remove-BCDataCacheExtension.md)
删除一个数据缓存文件。

### [Reset-BC](./Reset-BC.md)
将 BranchCache 重置为默认配置。

### [Set-BCAuthentication](./Set-BCAuthentication.md)
指定 BranchCache 计算机身份验证模式。

### [Set-BCCache](./Set-BCCache.md)
修改缓存文件配置。

### [Set-BCDataCacheEntryMaxAge](./Set-BCDataCacheEntryMaxAge.md)
修改数据能够在缓存中保留的最大时间长度。

### [Set-BCMinSMBLatency](./Set-BCMinSMBLatency.md)
设置客户端与服务器之间必须存在的最小延迟时间，才能使用透明缓存功能。

### [Set-BCSecretKey](./Set-BCSecretKey.md)
用于生成分段密钥（segment secrets）的加密密钥。


