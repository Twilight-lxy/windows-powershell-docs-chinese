---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfsclaimdescription?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsClaimDescription
---

# 设置 AdfsClaimDescription

## 摘要
修改索赔描述的属性。

## 语法

### 名称
```
Set-AdfsClaimDescription [-IsAccepted <Boolean>] [-IsOffered <Boolean>] [-IsRequired <Boolean>]
 [-Notes <String>] [-Name <String>] [-ClaimType <String>] [-ShortName <String>] [-TargetName] <String>
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 简称（ShortName）
```
Set-AdfsClaimDescription [-IsAccepted <Boolean>] [-IsOffered <Boolean>] [-IsRequired <Boolean>]
 [-Notes <String>] [-Name <String>] [-ClaimType <String>] [-ShortName <String>] [-TargetShortName] <String>
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 标识符
```
Set-AdfsClaimDescription [-IsAccepted <Boolean>] [-IsOffered <Boolean>] [-IsRequired <Boolean>]
 [-Notes <String>] [-Name <String>] [-ClaimType <String>] [-ShortName <String>] [-TargetClaimType] <String>
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject
```
Set-AdfsClaimDescription [-IsAccepted <Boolean>] [-IsOffered <Boolean>] [-IsRequired <Boolean>]
 [-Notes <String>] [-Name <String>] [-ClaimType <String>] [-ShortName <String>]
 [-TargetClaimDescription] <ClaimDescription> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AdfsClaimDescription` cmdlet 用于修改 Active Directory Federation Services (AD FS) 声明描述中的属性。

## 示例

### 示例 1：修改索赔描述的名称
```
PS C:\> Set-AdfsClaimDescription -TargetName "Role" -Name "RoleDesc"
```

这个命令将名为“Role”的索赔描述名称更改为“RoleDesc”。

## 参数

### -ClaimType
指定该声明的声明类型 URI（Uniform Resource Identifier）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IsAccepted
该字段用于指示声明是否作为被联邦服务（Federation Service）接受的声明，而被发布在联合体的元数据中。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IsOffered
该字段用于指示该声明是否作为联邦服务提供的声明被发布在联邦元数据中。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IsRequired
该字段用于指示声明是否已作为联邦服务所要求的声明被发布在联邦元数据中。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定要修改的声明的友好名称（即易于理解的名称）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Notes
用于指定描述索赔描述用途的文本。该cmdlet会将这些注释添加到索赔描述中。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

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

### -ShortName
指定用于生成和消费 JWT 令牌的声明描述的唯一简短名称标识符。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TargetClaimDescription
用于指定一个 **ClaimDescription** 对象。此 cmdlet 会修改您所指定的 **ClaimDescription** 对象。若要获取某个声明的描述信息，可以使用 **Get-AdfsClaimDescription** cmdlet。

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
指定要修改的声明描述中的声明类型。

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
指定要修改的声明描述的友好名称（即用户易于理解的名称）。

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
指定 AD FS 用于查找现有声明描述的简短名称标识符。

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
展示了如果该cmdlet运行会发生什么情况。但实际上，这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft IdentityServer.PowerShell.Resources.ClaimDescription

`TargetClaimDescription` 参数接收一个 `ClaimDescription` 对象。

### System.String

字符串对象通过 *TargetClaimType*、*TargetName* 和 *TargetShortName* 参数被接收。

## 输出

### Microsoft IdentityServer.PowerShell.Resources.ClaimDescription

当指定 *PassThru* 参数时，该命令会返回更新后的 ClaimDescription 对象。默认情况下，此cmdlet不会生成任何输出。

## 备注
* All Set-* cmdlets have a positional parameter (at position 0) with a name that starts with Target*. This parameter defines the search criteria, and the parameter set. For example, **Set-ADFSRelyingParty** has the parameters *TargetName*, *TargetIdentifierUri*, and *TargetRelyingParty*. You can use only one of these *Target** parameters to identify which RelyingParty to modify. Because these parameters are positional, you do not have to specify their name. Therefore, the following commands are identical in effect. The commands change the RelyingParty object named RP1 to RP2.

- `Set-ADFSRelyingParty -TargetName RP1Name -Name RP2Name`
- `Set-ADFSRelyingParty RP1Name -Name RP2Name`

## 相关链接

[Add-AdfsClaimDescription](./Add-AdfsClaimDescription.md)

[Get-AdfsClaimDescription](./Get-AdfsClaimDescription.md)

[Remove-AdfsClaimDescription](./Remove-AdfsClaimDescription.md)

