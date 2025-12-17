---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfsglobalauthenticationpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsGlobalAuthenticationPolicy
---

# Get-AdfsGlobalAuthenticationPolicy

## 摘要
显示 AD FS 全局策略。

## 语法

```
Get-AdfsGlobalAuthenticationPolicy [<CommonParameters>]
```

## 描述
`Get-AdfsGlobalAuthenticationPolicy` cmdlet 显示全局身份验证策略，该策略包括当前被允许作为额外提供者（additional providers）的提供者信息，这些提供者的详细信息存储在 `AdditionalAuthenticationProvider` 属性中。

## 示例

### 示例 1：显示全局认证策略
```
PS C:\> Get-AdfsGlobalAuthenticationPolicy


AdditionalAuthenticationProvider      : {MultiFactorAuthentication}
DeviceAuthenticationEnabled           : True
PrimaryIntranetAuthenticationProvider : {WindowsAuthentication}
PrimaryExtranetAuthenticationProvider : {FormsAuthentication, CertificateAuthentication}
WindowsIntegratedFallbackEnabled      : True
```

该命令用于显示全局身份验证策略。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### System.Object

## 备注

## 相关链接

[Set-AdfsGlobalAuthenticationPolicy](./Set-AdfsGlobalAuthenticationPolicy.md)

