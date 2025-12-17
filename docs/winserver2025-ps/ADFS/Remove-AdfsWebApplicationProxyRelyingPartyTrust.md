---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/remove-adfswebapplicationproxyrelyingpartytrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AdfsWebApplicationProxyRelyingPartyTrust
---

# 移除依赖于 AdfsWebApplicationProxy 的信任方（Remove-AdfsWebApplicationProxyRelyingPartyTrust）

## 摘要
移除了Web应用程序代理（Web Application Proxy）所依赖的信任对象（trust object）。

## 语法

```
Remove-AdfsWebApplicationProxyRelyingPartyTrust [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-AdfsWebApplicationProxyRelyingPartyTrust` cmdlet 用于删除 Web Application Proxy 的依赖方信任对象。如果删除了该信任对象，Web Application Proxy 将阻止所有通过代理的外部访问。如果您计划在以后重新创建该信任关系，请使用此 cmdlet。如果要暂时阻止通过代理的访问，可以使用 `Disable-AdfsWebApplicationProxyRelyingPartyTrust` cmdlet 来禁用依赖方信任对象。

Web应用程序代理（Web Application Proxy）所依赖的信任机制对于管理来自企业网络外部的全局网络访问非常有用。通过设置身份验证和授权策略，管理员可以限制对通过该Web应用程序代理发布的内部Web应用程序和服务的访问权限。

## 示例

#### 示例 1：移除对依赖方的信任
```
PS C:\> Remove-AdfsWebApplicationProxyRelyingPartyTrust
```

此命令会删除与 Web 应用程序代理相关的信任对象，从而阻止所有通过该代理访问 Web 应用程序的尝试。

## 参数

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并未被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[添加 AdfsWebApplicationProxy 依赖方信任关系](./Add-AdfsWebApplicationProxyRelyingPartyTrust.md)

[禁用 AdfsWebApplicationProxy 依赖方信任功能](./ Disable-AdfsWebApplicationProxyRelyingPartyTrust.md)

[Enable-AdfsWebApplicationProxyRelyingPartyTrust](./Enable-AdfsWebApplicationProxyRelyingPartyTrust.md)

[Get-AdfsWebApplicationProxyRelyingPartyTrust](./Get-AdfsWebApplicationProxyRelyingPartyTrust.md)

[Set-AdfsWebApplicationProxyRelyingPartyTrust](./Set-AdfsWebApplicationProxyRelyingPartyTrust.md)

