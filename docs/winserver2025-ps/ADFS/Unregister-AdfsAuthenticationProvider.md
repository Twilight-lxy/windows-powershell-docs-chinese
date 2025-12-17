---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/unregister-adfsauthenticationprovider?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Unregister-AdfsAuthenticationProvider
---

# 注销 AdfsAuthenticationProvider

## 摘要
从 AD FS 中删除外部身份验证提供程序。

## 语法

```
Unregister-AdfsAuthenticationProvider [-Name] <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Unregister-AdfsAuthenticationProvider` cmdlet 用于从 Active Directory Federation Services (AD FS) 中删除外部身份验证提供程序。可以使用 `Get-AdfsAuthenticationProvider` cmdlet 来获取已注册的身份验证提供程序列表。

## 示例

### 示例 1：删除已注册的身份验证提供者
```
PS C:\> Unregister-AdfsAuthenticationProvider -Name "ContosoExternalAuthProvider"
```

这个命令会删除名为 ContosoExternalAuthProvider 的附加身份验证提供者。

## 参数

### -Name
指定要从 AD FS 中删除的身份验证提供程序的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前，会提示您确认是否要执行该操作。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并未运行该cmdlet。

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
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### System.Object

## 备注

## 相关链接

[Get-AdfsAuthenticationProvider](./Get-AdfsAuthenticationProvider.md)

[注册 AdfsAuthenticationProvider](./Register-AdfsAuthenticationProvider.md)

