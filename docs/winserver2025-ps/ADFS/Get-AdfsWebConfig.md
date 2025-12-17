---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfswebconfig?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsWebConfig
---

# Get-AdfsWebConfig

## 摘要
获取 AD FS 网页自定义配置设置。

## 语法

```
Get-AdfsWebConfig [<CommonParameters>]
```

## 描述
`Get-AdfsWebConfig` cmdlet 用于获取 Active Directory Federation Services (AD FS) 的 Web 自定义配置设置。

## 示例

#### 示例 1：获取配置设置
```
PS C:\> Get-AdfsWebConfig

ActiveThemeName      : Default
CDCCookieReader      :
CDCCookieWriter      :
HRDCookieLifetime    : 30
HRDCookieEnabled     : True
ContextCookieEnabled : True
```

这个命令用于获取网页自定义配置设置。

## 参数

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.IdentityServer.Management.Resources.AdfsWebConfig
此cmdlet生成一个**AdfsWebConfig**对象，该对象表示AD FS Web自定义配置设置。该对象包含以下属性：

- ActiveThemeName: **System.String**
- CDCCookieReader: **System.Uri**
- CDCCookieWriter: **System.Uri**
- HRDCookieLifetime: **System.Int32**
- HRDCookieEnabled: **System.Boolean**
- ContextCookieEnabled: **System.Boolean**

## 备注

## 相关链接

[Set-AdfsWebConfig](./Set-AdfsWebConfig.md)

