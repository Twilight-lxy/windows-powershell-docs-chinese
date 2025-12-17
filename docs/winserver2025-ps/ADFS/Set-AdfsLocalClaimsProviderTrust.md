---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfslocalclaimsprovidertrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsLocalClaimsProviderTrust
---

# 设置 AdfsLocalClaimsProviderTrust

## 摘要
修改本地声明提供者（claims provider）的信任设置。

## 语法

### 标识符Object
```
Set-AdfsLocalClaimsProviderTrust [-AcceptanceTransformRules <String>] [-AcceptanceTransformRulesFile <String>]
 [-Name <String>] [-Notes <String>] [-OrganizationalAccountSuffix <String[]>] [-Force]
 -TargetClaimsProviderTrust <LocalClaimsProviderTrust> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 标识符
```
Set-AdfsLocalClaimsProviderTrust [-AcceptanceTransformRules <String>] [-AcceptanceTransformRulesFile <String>]
 [-Name <String>] [-Notes <String>] [-OrganizationalAccountSuffix <String[]>] [-Force]
 -TargetIdentifier <String> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 标识符Name
```
Set-AdfsLocalClaimsProviderTrust [-AcceptanceTransformRules <String>] [-AcceptanceTransformRulesFile <String>]
 [-Name <String>] [-Notes <String>] [-OrganizationalAccountSuffix <String[]>] [-Force] -TargetName <String>
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AdfsLocalClaimsProviderTrust` cmdlet 用于修改本地声明提供者的信任关系。有关更多信息，请参阅 `Add-AdfsLocalClaimsProviderTrust` cmdlet 的文档。

## 示例

## 参数

### -AcceptanceTransformRules
指定了一组需要在本地声明提供者信任关系中配置的声明规则。这些规则决定了从由本地声明提供者信任关系所代表的合作伙伴那里接收的信息内容。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AcceptanceTransformRulesFile
指定一个文件的完整路径，该文件包含了用于配置本地声明提供者信任机制的声明规则集。

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

### -Force
强制命令运行，而无需请求用户确认。

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

### -Name
为本地声明提供者信任关系指定一个名称。

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
用于指定注释信息。

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

### -OrganizationalAccountSuffix
指定一组组织账户后缀，管理员可以为这些后缀配置信任设置，以便在“家庭领域发现”（Home Realm Discovery，简称 HRD）场景中使用这些后缀与身份验证提供者进行交互。

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

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -TargetClaimsProviderTrust
用于指定需要修改的本地claims提供者信任关系。要获取一个**LocalClaimsProviderTrust**对象，可以使用**Get-AdfsLocalClaimsProviderTrust** cmdlet。

```yaml
Type: LocalClaimsProviderTrust
Parameter Sets: IdentifierObject
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetIdentifier
指定要修改的本地声明提供者信任关系的ID。

```yaml
Type: String
Parameter Sets: Identifier
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetName
指定要修改的本地声明提供者信任关系的名称。

```yaml
Type: String
Parameter Sets: IdentifierName
Aliases:

Required: True
Position: Named
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
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Add-AdfsLocalClaimsProviderTrust](./Add-AdfsLocalClaimsProviderTrust.md)

[禁用 AdfsLocalClaimsProviderTrust](./Disable-AdfsLocalClaimsProviderTrust.md)

[Enable-AdfsLocalClaimsProviderTrust](./Enable-AdfsLocalClaimsProviderTrust.md)

[Get-AdfsLocalClaimsProviderTrust](./Get-AdfsLocalClaimsProviderTrust.md)

[Remove-AdfsLocalClaimsProviderTrust](./Remove-AdfsLocalClaimsProviderTrust.md)

