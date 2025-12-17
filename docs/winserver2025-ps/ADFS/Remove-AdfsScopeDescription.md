---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/remove-adfsscopedescription?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AdfsScopeDescription
---

# 删除 AdfsScopeDescription

## 摘要
删除 AD FS 中的作用域描述（scope description）。

## 语法

### 名称
```
Remove-AdfsScopeDescription [-TargetName] <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject
```
Remove-AdfsScopeDescription [-InputObject] <OAuthScopeDescription> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-AdfsScopeDescription` cmdlet 用于删除表示在 Active Directory Federation Services (AD FS) 中授予资源和应用程序的访问范围的描述信息。

## 示例

## 参数

### -InputObject
指定此cmdlet要删除的范围描述。

```yaml
Type: OAuthScopeDescription
Parameter Sets: InputObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetName
指定此cmdlet要删除的作用域描述名称。

```yaml
Type: String
Parameter Sets: Name
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前会提示您进行确认。

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
展示了如果该cmdlet被运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.IdentityServer.ManagementResources.OAuthScopeDescription

`OAuthScopeDescription` 对象是通过 `InputObject` 参数接收到的。

### System.String

字符串对象是通过*TargetName*参数接收到的。

## 输出

## 备注

## 相关链接

[Add-AdfsScopeDescription](./Add-AdfsScopeDescription.md)

[Get-AdfsScopeDescription](./Get-AdfsScopeDescription.md)

[Set-AdfsScopeDescription](./Set-AdfsScopeDescription.md)

