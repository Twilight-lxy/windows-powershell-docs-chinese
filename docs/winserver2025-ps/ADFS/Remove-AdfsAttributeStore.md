---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/remove-adfsattributestore?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AdfsAttributeStore
---

# 移除 AdfsAttributeStore

## 摘要
从联邦服务中删除一个属性存储（attribute store）。

## 语法

### 名称
```
Remove-AdfsAttributeStore [-TargetName] <String> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

请帮我将以下Markdown格式转换为中文：  

### InputObject
```
Remove-AdfsAttributeStore [-TargetAttributeStore] <AttributeStore> [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-AdfsAttributeStore` cmdlet 用于从联邦服务中删除属性存储（attribute store）。

## 示例

#### 示例 1：删除属性存储（Attribute Store）
```
PS C:\> Remove-ADFSAttributeStore -TargetName "ContosoAttributeStore01"
```

此命令从联合服务中删除名为 ContosoAttributeStore01 的属性存储。

## 参数

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

### -TargetAttributeStore
指定一个 **AttributeStore** 对象。该 cmdlet 会删除你指定的 **AttributeStore** 对象。若要获取属性存储，可以使用 **Get-AdfsAttributeStore** cmdlet。

```yaml
Type: AttributeStore
Parameter Sets: InputObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetName
指定要删除的属性存储的名称。

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

### MicrosoftIdentityServer.PowerShell.Resources AttributeStore

`TargetName` 参数接收一个 `AttributeStore` 对象。

## 输出

### 无，或为 `Microsoft.IdentityServerManagement.Resources.AttributeStore`

当指定 *PassThru* 参数时，会返回被移除的 AttributeStore 对象。默认情况下，此 cmdlet 不会生成任何输出。

## 备注
* An Active Directory Federation Services (AD FS) 2.0 attribute store is a pluggable module that the policy process for AD FS 2.0 can query to retrieve claim values. You can use either an Active Directory database or a Microsoft SQL Server database as your attribute store, or you can implement your own custom attribute store.

## 相关链接

[Get-AdfsAttributeStore](./Get-AdfsAttributeStore.md)

[Add-AdfsAttributeStore](./Add-AdfsAttributeStore.md)

[Set-AdfsAttributeStore](./Set-AdfsAttributeStore.md)

