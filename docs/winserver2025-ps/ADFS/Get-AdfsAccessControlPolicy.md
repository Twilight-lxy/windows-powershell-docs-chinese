---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfsaccesscontrolpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsAccessControlPolicy
---

# Get-AdfsAccessControlPolicy

## 摘要
获取一个 AD FS 访问控制策略。

## 语法

```
Get-AdfsAccessControlPolicy [-Name <String[]>] [-Identifier <String[]>] [<CommonParameters>]
```

## 描述
`Get-AdfsAccessControlPolicy` cmdlet 用于获取 Active Directory Federation Services (AD FS) 的访问控制策略。

## 示例

## 参数

### -Identifier
指定一个ID数组。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定一个策略名称数组。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[新 AdfsAccessControlPolicy](./New-AdfsAccessControlPolicy.md)

[Remove-AdfsAccessControlPolicy](./Remove-AdfsAccessControlPolicy.md)

[Set-AdfsAccessControlPolicy](./Set-AdfsAccessControlPolicy.md)

