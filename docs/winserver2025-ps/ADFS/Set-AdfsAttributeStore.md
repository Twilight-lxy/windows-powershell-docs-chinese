---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfsattributestore?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsAttributeStore
---

# 设置 AdfsAttributeStore

## 摘要
修改属性存储（attribute store）的属性。

## 语法

### 名称
```
Set-AdfsAttributeStore [-Name <String>] [-Configuration <Hashtable>] [-TargetName] <String> [-PassThru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject
```
Set-AdfsAttributeStore [-Name <String>] [-Configuration <Hashtable>] [-TargetAttributeStore] <AttributeStore>
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AdfsAttributeStore` cmdlet 用于修改联邦服务中属性存储的属性。

## 示例

### 示例 1：修改属性存储的配置
```
PS C:\> Set-AdfsAttributeStore -TargetName "ContosoAttributeStore01" -Configuration @{"runmode" = "verbose"; configParaName2 = configParaValueNew}
```

此命令用于修改名为 ContosoAttributeStore01 的自定义属性存储的配置。

## 参数

### -Configuration
指定属性存储的初始化参数，例如连接字符串。

```yaml
Type: Hashtable
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定该属性存储的友好名称（即用户友好的名称）。

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
指定一个 **AttributeStore** 对象。该 cmdlet 会修改您指定的属性存储。要获取属性存储，请使用 **Get-AdfsAttributeStore** cmdlet。

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
指定要修改的属性存储的名称。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[添加 AdfsAttributeStore](./Add-AdfsAttributeStore.md)

[Get-AdfsAttributeStore](./Get-AdfsAttributeStore.md)

[Remove-AdfsAttributeStore](./Remove-AdfsAttributeStore.md)

