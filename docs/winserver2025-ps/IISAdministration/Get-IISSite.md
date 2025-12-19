---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/get-iissite?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IISSite
---

# 获取 IISSite

## 摘要
获取IIS网站的配置信息。

## 语法

```
Get-IISSite [[-Name] <String[]>] [<CommonParameters>]
```

## 描述
`Get-IISSite` cmdlet 可以获取有关 Internet Information Services (IIS) 网站的信息，包括它们的当前状态以及其他关键数据。如果您请求某个特定的网站或通过逗号分隔的网站列表，那么只会返回那些名称作为参数传递的网站；否则，将返回所有网站的信息。

## 示例

#### 示例 1：获取有关 IIS 网站的信息
```
PS C:\> Get-IISSite "Default Web Site"
```

这个命令用于获取默认网站（Default Web Site）的配置信息。

### 示例 2：获取所有 IIS 网站的信息
```
PS C:\> Get-IISSite
Name             ID   State      Physical Path                  Bindings
----             --   -----      -------------                  --------
Default Web Site 1    Started    %SystemDrive%\inetpub\wwwroot  http *:80:
PattiFul         2    Stopped    C:\inetpub\PattiFul            http *:8080:
                                                                http *:8033:
FTPSite          3               C:\inetpub\ftproot             ftp *:21:
DavidChe         4    Started    c:\                            http *:8088:
MyNewSite        6555 Started    C:\inetpub\wwwroot             http *:8099:
                                                                http *:8022:
```

这个命令可以获取所有 IIS 网站的所有配置信息。

### 示例 3：获取 IIS 网站的某个属性
```
PS C:\> $Site = Get-IISSite "Default Web Site"
PS C:\> $Site.Attributes["ServerAutoStart"]
IsInheritedFromDefaultValue : True
IsProtected                 : False
Name                        : serverAutoStart
Schema                      : Microsoft.Web.Administration.ConfigurationAttributeSchema
Value                       : True
```

这个命令用于获取 IIS 默认网站的 ServerAutoStart 属性。

## 参数

### -Name
指定要获取配置信息的 IIS 网站的名称。如果未使用此参数，则会返回所有网站的信息。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### System.String[]

## 输出

### System.Object

## 备注

## 相关链接

[New-IISSite](./New-IISSite.md)

[删除 IISSite](./Remove-IISSite.md)

[开始使用 IISS 服务](./Start-IISSite.md)

[停止使用 IISS 网站](./Stop-IISSite.md)

[用于 Windows PowerShell 的 IIS 管理 cmdlet](./iisadministration.md)

