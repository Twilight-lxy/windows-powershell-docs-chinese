---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfsadditionalauthenticationrule?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsAdditionalAuthenticationRule
---

# 获取 Adfs 额外身份验证规则

## 摘要
检索用于触发调用其他身份验证提供程序的全局规则。

## 语法

```
Get-AdfsAdditionalAuthenticationRule [<CommonParameters>]
```

## 描述
**Get-AdfsAdditionalAuthenticationRule** cmdlet 用于检索那些管理所有需要调用额外身份验证提供程序的应用程序的全局规则。当声明引擎评估这些额外身份验证规则并确定需要进行多因素身份验证时，系统会提示用户完成额外的身份验证过程。只有当您的所有应用程序都能通过 Active Directory Federation Services (AD FS) 实现基于 Web 的凭据收集时，才应使用此规则。如果由于规则的评估结果导致触发条件为真，那么使用 WS-Trust 等协议的应用程序将无法获取安全令牌。

## 示例

### 示例 1：获取全局额外的身份验证规则
```
PS C:\> Get-AdfsAdditionalAuthenticationRule
c:[Type == "http://schemas.microsoft.com/2012/01/devicecontext/claims/isregistereduser", Value == "false"]
=> issue(Type = "http://schemas.microsoft.com/ws/2008/06/identity/claims/authenticationmethod", Value = "http://schemas.microsoft.com/claims/multipleauthn");

c:[Type == "http://schemas.microsoft.com/ws/2012/01/insidecorporatenetwork", Value == "false"]
=> issue(Type = "http://schemas.microsoft.com/ws/2008/06/identity/claims/authenticationmethod", Value = "http://schemas.microsoft.com/claims/multipleauthn");
```

此命令用于检索为 AD FS 配置的全局附加身份验证规则。命令的输出显示，所有外部网络访问以及所有未连接到工作场所的设备都需要进行多因素身份验证。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Set-AdfsAdditionalAuthenticationRule](./Set-AdfsAdditionalAuthenticationRule.md)

