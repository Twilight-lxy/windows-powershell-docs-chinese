---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/add-adfsclaimsprovidertrustsgroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-AdfsClaimsProviderTrustsGroup
---

# 添加 AdfsClaimsProviderTrustsGroup

## 摘要
根据包含多个实体的元数据创建一个声明提供者信任组（claims provider trust group）。

## 语法

### MetadataFile
```
Add-AdfsClaimsProviderTrustsGroup -MetadataFile <String> [-Force] [-PassThru]
 [-AcceptanceTransformRules <String>] [-AcceptanceTransformRulesFile <String>] [-MonitoringEnabled <Boolean>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### MetadataUrl
```
Add-AdfsClaimsProviderTrustsGroup -MetadataUrl <Uri> [-AutoUpdateEnabled <Boolean>] [-Force] [-PassThru]
 [-AcceptanceTransformRules <String>] [-AcceptanceTransformRulesFile <String>] [-MonitoringEnabled <Boolean>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-AdfsClaimsProviderTrustsGroup` cmdlet 根据包含多个实体的元数据来创建一个声明提供者信任组。

## 示例

### 示例 1：通过元数据 URL 添加信任组
```
PS C:\> Add-AdfsClaimsProviderTrustsGroup -MetadataUrl https://www.contosoconsortium.com/metadata/metadata.xml
```

此命令指定了一个元数据URL，用于添加信任组。

### 示例 2：通过元数据文件添加一个信任组
```
PS C:\> Add-AdfsClaimsProviderTrustsGroup -MetadataFile "C:\metadata.xml"
```

此命令指定一个元数据文件，用于添加信任组。

## 参数

### -AcceptanceTransformRules
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

### -AutoUpdateEnabled
表示是否启用了自动更新功能。

```yaml
Type: Boolean
Parameter Sets: MetadataUrl
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
强制命令执行，而无需请求用户确认。

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

### -MetadataFile
指定本地文件系统中元数据文件的路径和名称。

```yaml
Type: String
Parameter Sets: MetadataFile
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MetadataUrl
指定一个在公共互联网上可获取的元数据文件的URL。

```yaml
Type: Uri
Parameter Sets: MetadataUrl
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MonitoringEnabled
表示是否启用了监控功能。

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

### -Confirm
在运行cmdlet之前，会提示您进行确认。

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
展示了如果该cmdlet运行会发生的情景。但实际上这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-AdfsClaimsProviderTrustsGroup](./Get-AdfsClaimsProviderTrustsGroup.md)

[Remove-AdfsClaimsProviderTrustsGroup](./Remove-AdfsClaimsProviderTrustsGroup.md)

