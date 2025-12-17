---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfssslcertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsSslCertificate
---

# 获取 AdFS SSL 证书

## 摘要
获取为 AD FS 和设备注册服务配置的 SSL 绑定的主机名、端口以及证书哈希值。

## 语法

```
Get-AdfsSslCertificate [<CommonParameters>]
```

## 描述
`Get-AdfsSslCertificate` cmdlet 可获取为 Active Directory Federation Services (AD FS) 配置的所有 SSL 绑定的主机名、端口和证书哈希值；如果设备注册服务已启用，该 cmdlet 也会获取相关信息。

## 示例

### 示例 1：获取 SSL 绑定的相关信息
```
PS C:\> Get-AdfsSslCertificate
HostName                           PortNumber  CertificateHash
--------                           ----------  ---------------
sts.contoso100.com                    443      4195EE03C2721F7478B67E94BD83BB373FE22D98
localhost                             443      4195EE03C2721F7478B67E94BD83BB373FE22D98
sts.contoso100.com                   49443     4195EE03C2721F7478B67E94BD83BB373FE22D98
EnterpriseRegistration.contoso...     443      4195EE03C2721F7478B67E94BD83BB373FE22D98
```

这个命令可以获取所有已配置的SSL绑定的主机名、端口号以及证书哈希值。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Set-AdfsSslCertificate](./Set-AdfsSslCertificate.md)

