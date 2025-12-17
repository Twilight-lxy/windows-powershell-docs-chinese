---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/disable-adfslocalclaimsprovidertrust?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-AdfsLocalClaimsProviderTrust
---

# 禁用 AdfsLocalClaimsProviderTrust

## 摘要
禁用对本地声明提供者的信任。

## 语法

### 标识符Object
```
Disable-AdfsLocalClaimsProviderTrust -TargetClaimsProviderTrust <LocalClaimsProviderTrust> [-PassThru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 标识符
```
Disable-AdfsLocalClaimsProviderTrust -TargetIdentifier <String> [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 标识符Name
```
Disable-AdfsLocalClaimsProviderTrust -TargetName <String> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Disable-AdfsLocalClaimsProviderTrust` cmdlet 用于禁用对本地声明提供者的信任（即停止使用该本地声明提供者进行身份验证或授权操作）。

## 示例

### 示例 1：禁用对本地声明提供者的信任
```
PS C:\> Disable-AdfsLocalClaimsProviderTrust -TargetName "testldap"
```

此命令会禁用一个名为“test ldap”的本地声明提供者信任（local claims provider trust）。

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

### -TargetClaimsProviderTrust
用于指定要禁用的本地声明提供者信任关系（local claims provider trust）。若要获取一个 **LocalClaimsProviderTrust** 对象，可以使用 **Get-AdfsLocalClaimsProviderTrust** cmdlet。

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
指定要禁用的本地声明提供者信任（local claims provider trust）的ID。

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
指定要禁用的本地声明提供程序信任关系的名称。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Add-AdfsLocalClaimsProviderTrust](./Add-AdfsLocalClaimsProviderTrust.md)

[Enable-AdfsLocalClaimsProviderTrust](./Enable-AdfsLocalClaimsProviderTrust.md)

[Get-AdfsLocalClaimsProviderTrust](./Get-AdfsLocalClaimsProviderTrust.md)

[Remove-AdfsLocalClaimsProviderTrust](./Remove-AdfsLocalClaimsProviderTrust.md)

[Set-AdfsLocalClaimsProviderTrust](./Set-AdfsLocalClaimsProviderTrust.md)

