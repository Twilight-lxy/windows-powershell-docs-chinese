---
description: 使用此主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfsaccesscontrolpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsAccessControlPolicy
---

# 设置 AdfsAccessControlPolicy

## 摘要
修改 AD FS 访问控制策略。

## 语法

### 标识符Name
```
Set-AdfsAccessControlPolicy [-Name <String>] [-Identifier <String>] [-Description <String>]
 [-PolicyMetadata <PolicyMetadata>] [-PolicyMetadataFile <String>] [-PassThru] [-TargetName] <String> [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### 标识符
```
Set-AdfsAccessControlPolicy [-Name <String>] [-Identifier <String>] [-Description <String>]
 [-PolicyMetadata <PolicyMetadata>] [-PolicyMetadataFile <String>] [-PassThru] [-TargetIdentifier] <String>
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 标识符Object
```
Set-AdfsAccessControlPolicy [-Name <String>] [-Identifier <String>] [-Description <String>]
 [-PolicyMetadata <PolicyMetadata>] [-PolicyMetadataFile <String>] [-PassThru]
 [-TargetAccessControlPolicy] <AdfsAccessControlPolicy> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AdfsAccessControlPolicy` cmdlet 用于修改 Active Directory Federation Services (AD FS) 的访问控制策略。

## 示例

## 参数

### -Description
为该策略指定一个描述。

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

### -Identifier
为该策略指定一个ID。

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

### -Name
为该策略指定一个名称。

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
返回一个表示您正在操作的项的对象。默认情况下，此 cmdlet 不生成任何输出。

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

### -PolicyMetadata
为策略指定元数据。

```yaml
Type: PolicyMetadata
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PolicyMetadataFile
指定用于该策略的元数据文件。

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

### -TargetAccessControlPolicy
```yaml
Type: AdfsAccessControlPolicy
Parameter Sets: IdentifierObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetIdentifier
指定目标的ID。

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
指定目标名称。

```yaml
Type: String
Parameter Sets: IdentifierName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
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
展示了如果该cmdlet运行会发生什么情况。但实际上这个cmdlet并没有被运行。

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

[Get-AdfsAccessControlPolicy](./Get-AdfsAccessControlPolicy.md)

[New-AdfsAccessControlPolicy](./New-AdfsAccessControlPolicy.md)

[Remove-AdfsAccessControlPolicy](./Remove-AdfsAccessControlPolicy.md)

