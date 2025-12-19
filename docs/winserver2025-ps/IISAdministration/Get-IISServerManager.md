---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/get-iisservermanager?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IISServerManager
---

# 获取 IISServerManager

## 摘要
获取 IIS ServerManager 的 IISAdministration 视图。

## 语法

```
Get-IISServerManager [<CommonParameters>]
```

## 描述
**Get-IISServerManager** cmdlet 从 Microsoft.Web ADMINISTRATION 中获取 Internet Information Services (IIS) 服务器管理对象。

## 示例

### 示例 1：获取一个处于活动状态的 `Microsoft.Web Administration.ServerManager` 对象
```
PS C:\> $SM = Get-IISServerManager
```

这个命令获取当前活动的 Microsoft.Web.Administration.ServerManager 对象，并将结果存储在变量 $SM 中。

### 示例 2：使用 ServerManager 对象获取站点对象并列出 IIS 网站
```
PS C:\> $SM = Get-IISServerManager
PS C:\> $Sites = $SM.Sites
PS C:\> $Sites
Name             ID   State      Physical Path                  Bindings
----             --   -----      -------------                  --------
Default Web Site 1    Stopped    %SystemDrive%\inetpub\wwwroot  http *:80:
Patti            2    Started    C:\inetpub\Patti               http *:8080:
                                                                http *:8033:

FTPSite          3               C:\inetpub\ftproot             ftp *:21:
DavidChe         4    Started    c:\                            http *:8088:
MyNewSite        6555 Started    C:\inetpub\wwwroot             http *:8099:
                                                                http *:8022:
TestSite         5    Stopped    C:\inetpub\testsite            http *:8080:
```

这个命令通过使用 ServerManager 对象来获取站点对象，并列出所有的 IIS 网站。

### 示例 3：使用 ServerManager 对象获取应用程序池对象并回收某个应用程序池。
```
PS C:\> $SM = Get-IISServerManager
PS C:\> $SM.ApplicationPools["PattiFul"].Recycle()
```

这个命令使用 ServerManager 对象来获取应用程序池对象，然后对应用程序池进行回收（即重新分配资源）。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于公有参数（about_CommonParameters）（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

