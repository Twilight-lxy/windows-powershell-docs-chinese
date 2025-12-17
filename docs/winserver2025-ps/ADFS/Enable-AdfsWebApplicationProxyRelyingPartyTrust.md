---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/enable-adfswebapplicationproxyrelyingpartytrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-AdfsWebApplicationProxyRelyingPartyTrust
---

# 启用 AdfsWebApplicationProxy 依赖方信任

## 摘要
启用Web应用程序代理的依赖方信任对象。

## 语法

```
Enable-AdfsWebApplicationProxyRelyingPartyTrust [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Enable-AdfsWebApplicationProxyRelyingPartyTrust` 这个 cmdlet 用于启用 Web 应用程序代理的依赖方信任对象。如果您之前使用 `Disable-AdfsWebApplicationProxyRelyingPartyTrust` cmdlet 暂时禁用了所有外部访问，那么就可以使用这个 cmdlet 来重新启用这些功能。

Web应用程序代理（Web Application Proxy）所依赖的信任机制有助于管理来自企业外部网络的全球网络访问。通过设置身份验证和授权策略，管理员可以限制对通过该Web应用程序代理发布的内部Web应用程序和服务的访问。

## 示例

### 示例 1：为 Web 应用程序代理启用依赖方信任
```
PS C:\> Enable-AdfsWebApplicationProxyRelyingPartyTrust
```

此命令用于启用Web应用程序代理的依赖方信任对象（trust object）。

## 参数

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此 cmdlet 不会生成任何输出。

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
在运行该 cmdlet 之前，会提示您进行确认。

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
展示了如果该cmdlet运行会发生什么情况。不过实际上这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[添加 AdfsWebApplicationProxyRelyingPartyTrust](./Add-AdfsWebApplicationProxyRelyingPartyTrust.md)

[禁用 AdfsWebApplicationProxy 依赖方信任](./Disable-AdfsWebApplicationProxyRelyingPartyTrust.md)

[Get-AdfsWebApplicationProxyRelyingPartyTrust](./Get-AdfsWebApplicationProxyRelyingPartyTrust.md)

[Remove-AdfsWebApplicationProxyRelyingPartyTrust](./Remove-AdfsWebApplicationProxyRelyingPartyTrust.md)

[Set-AdfsWebApplicationProxyRelyingPartyTrust](./Set-AdfsWebApplicationProxyRelyingPartyTrust.md)

