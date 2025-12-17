---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/remove-adfsclaimdescription?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AdfsClaimDescription
---

# 删除 AdFS ClaimDescription

## 摘要
从联邦服务中删除一个声明描述（claim description）。

## 语法

### 名称
```
Remove-AdfsClaimDescription [-TargetName] <String> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ShortName
```
Remove-AdfsClaimDescription [-TargetShortName] <String> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 标识符
```
Remove-AdfsClaimDescription [-TargetClaimType] <String> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject
```
Remove-AdfsClaimDescription [-TargetClaimDescription] <ClaimDescription> [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-AdfsClaimDescription` cmdlet 用于从联邦服务中删除某个声明描述（claim description）。

## 示例

### 示例 1：删除声明描述
```
PS C:\> Remove-AdfsClaimDescription -TargetName "Role"
```

此命令会删除名为“Role”的声明描述。

## 参数

### -PassThru
返回一个表示您正在操作的该项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -TargetClaimDescription
用于指定一个 **ClaimDescription** 对象。该 cmdlet 会删除您指定的 **ClaimDescription** 对象。若要获取声明描述信息，请使用 **Get-AdfsClaimDescription** cmdlet。

```yaml
Type: ClaimDescription
Parameter Sets: InputObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetClaimType
指定要删除的声明描述中的声明类型。

```yaml
Type: String
Parameter Sets: Identifier
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetName
指定要删除的索赔描述名称。

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

### -TargetShortName
指定 AD FS 用于查找现有声明描述的简称（ID）。

```yaml
Type: String
Parameter Sets: ShortName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.IdentityServer.PowerShell.Resources.ClaimDescription

`*TargetClaimDescription*` 参数接收了一个 `ClaimDescription` 对象。

### System.String

字符串对象通过 *TargetClaimType*、*TargetName* 和 *TargetShortName* 参数被接收。

## 输出

### Microsoft.IdentityServer.PowerShell.Resources.ClaimDescription

当指定*PassThru*参数时，会返回被移除的ClaimDescription对象。默认情况下，此cmdlet不会生成任何输出。

### 无

## 备注
* Use claim descriptions to configure the list of claims that are available to be offered or accepted by the Active Directory Federation Services (AD FS).

## 相关链接

[Add-AdfsClaimDescription](./Add-AdfsClaimDescription.md)

[Get-AdfsClaimDescription](./Get-AdfsClaimDescription.md)

[Set-AdfsClaimDescription](./Set-AdfsClaimDescription.md)

