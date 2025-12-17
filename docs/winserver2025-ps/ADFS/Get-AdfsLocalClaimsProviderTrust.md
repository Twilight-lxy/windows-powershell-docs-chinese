---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfslocalclaimsprovidertrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsLocalClaimsProviderTrust
---

# 获取 AdfsLocalClaimsProviderTrust

## 摘要
获取本地的声明提供者信任信息（即本地声明提供者的身份验证和授权机制）。

## 语法

### ClaimsProviderName（默认值）
```
Get-AdfsLocalClaimsProviderTrust [[-Name] <String[]>] [<CommonParameters>]
```

### 标识符
```
Get-AdfsLocalClaimsProviderTrust [-Identifier] <String[]> [<CommonParameters>]
```

## 描述
`Get-AdfsLocalClaimsProviderTrust` cmdlet 用于获取本地声明提供者信任关系（local claims provider trusts）。请指定要获取的信任关系的名称或 ID。

## 示例

## 参数

### -Identifier
指定一个包含要获取的本地声明提供程序信任关系的ID数组。

```yaml
Type: String[]
Parameter Sets: Identifier
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Name
指定一个数组，其中包含需要获取的本地声明提供者信任关系的名称。

```yaml
Type: String[]
Parameter Sets: ClaimsProviderName
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Add-AdfsLocalClaimsProviderTrust](./Add-AdfsLocalClaimsProviderTrust.md)

[禁用 AdfsLocalClaimsProviderTrust](./Disable-AdfsLocalClaimsProviderTrust.md)

[Enable-AdfsLocalClaimsProviderTrust](./Enable-AdfsLocalClaimsProviderTrust.md)

[Remove-AdfsLocalClaimsProviderTrust](./Remove-AdfsLocalClaimsProviderTrust.md)

[Set-AdfsLocalClaimsProviderTrust](./Set-AdfsLocalClaimsProviderTrust.md)

