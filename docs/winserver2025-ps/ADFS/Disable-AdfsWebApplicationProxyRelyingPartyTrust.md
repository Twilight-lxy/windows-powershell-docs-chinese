---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/disable-adfswebapplicationproxyrelyingpartytrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-AdfsWebApplicationProxyRelyingPartyTrust
---

# 禁用 AdfsWebApplicationProxy 依赖的 Party Trust 功能

## 摘要
禁用对 Web 应用程序代理的依赖方信任（即取消对该代理的可信性验证）。

## 语法

```
Disable-AdfsWebApplicationProxyRelyingPartyTrust [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Disable-AdfsWebApplicationProxyRelyingPartyTrust` cmdlet 用于禁用 Web 应用程序代理的依赖方信任对象。使用此 cmdlet 可以暂时阻止所有通过该代理访问 Web 应用程序的尝试。要恢复访问权限，请使用 `Enable-AdfsWebApplicationProxyRelyingPartyTrust` cmdlet。

基于Web应用程序代理的依赖方信任机制有助于管理来自企业网络外部的全球网络访问。通过设置身份验证和授权策略，管理员可以限制对通过Web应用程序代理发布的内部Web应用程序和服务的访问权限。

## 示例

### 示例 1：禁用通过代理的访问
```
PS C:\> Disable-AdfsWebApplicationProxyRelyingPartyTrust
```

此命令会禁用对代理的“依赖方信任”设置（relying party trust），从而阻止外部通过该代理访问网页应用程序。

## 参数

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此 cmdlet 不生成任何输出。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您进行确认。

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
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Add-AdfsWebApplicationProxyRelyingPartyTrust](./Add-AdfsWebApplicationProxyRelyingPartyTrust.md)

[Enable-AdfsWebApplicationProxyRelyingPartyTrust](./Enable-AdfsWebApplicationProxyRelyingPartyTrust.md)

[Get-AdfsWebApplicationProxyRelyingPartyTrust](./Get-AdfsWebApplicationProxyRelyingPartyTrust.md)

[Remove-AdfsWebApplicationProxyRelyingPartyTrust](./Remove-AdfsWebApplicationProxyRelyingPartyTrust.md)

[Set-AdfsWebApplicationProxyRelyingPartyTrust](./Set-AdfsWebApplicationProxyRelyingPartyTrust.md)

