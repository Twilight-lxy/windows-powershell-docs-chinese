---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.KeyDistributionService.Cmdlets.dll-Help.xml
Module Name: KDS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/kds/add-kdsrootkey?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-KdsRootKey
---

# Add-KdsRootKey

## 摘要
为 Microsoft Group KdsSvc 在 Active Directory 中生成一个新的根密钥。

## 语法

### EffectiveTime（默认值）
```
Add-KdsRootKey [-LocalTestOnly] [[-EffectiveTime] <DateTime>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### EffectiveImmediately
```
Add-KdsRootKey [-LocalTestOnly] [-EffectiveImmediately] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-KdsRootKey` cmdlet 为 Active Directory 中的 Microsoft 组密钥分发服务（KdsSvc）生成一个新的根密钥。Microsoft 组密钥分发服务会使用这个新的根密钥来生成新的组密钥。每个林（forest）只需要运行此命令一次即可。

## 示例

### 示例 1：生成一个新的根密钥
```
PS C:\> Add-KdsRootKey
```

此命令为 Microsoft Group KdsSvc 在 Active Directory 中生成一个新的根密钥。

### 示例 2：生成一个新的根密钥以供立即使用
```
PS C:\> Add-KdsRootKey -EffectiveImmediately
```

此命令会立即生成一个新的根密钥，并将其添加到 Microsoft Group KdsSvc 中。

### 示例 3：生成一个新的根密钥，并使其在特定日期生效
```
PS C:\> Add-KdsRootKey -EffectiveTime 03/23/2013
```

此命令为 Microsoft Group KdsSvc 生成一个新的根密钥，该密钥将于 2013 年 3 月 23 日生效。请使用 mm/dd/yyyy 的格式来指定日期。

### 示例 4：仅在本地主机上生成一个新的根密钥
```
PS C:\> Add-KdsRootKey -LocalTestOnly
```

此命令仅会在本地主机上生成一个新的根密钥。

## 参数

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

### -EffectiveImmediately
表示 Microsoft 组键分发服务会立即使用新的根密钥。

```yaml
Type: SwitchParameter
Parameter Sets: EffectiveImmediately
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EffectiveTime
指定新生成的根密钥生效的日期。如果未指定此参数，则默认日期为当前日期后的10天。

```yaml
Type: DateTime
Parameter Sets: EffectiveTime
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -LocalTestOnly
表示新的根密钥仅在本地主机上生成。此参数与 **Set-KdsConfiguration** cmdlet 一起使用，用于测试本地服务器的配置。

如果指定了这个参数，那么该cmdlet会返回一个值，表示测试是否通过。

如果未指定此参数，则当操作成功时，该cmdlet会返回根键的标识符（ID）。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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

### 无
此cmdlet不接受任何输入对象。

## 输出

### System(Boolean)

### System.Guid

## 备注

## 相关链接

[Clear-KdsCache](./Clear-KdsCache.md)

[Get-KdsConfiguration](./Get-KdsConfiguration.md)

[Get-KdsRootKey](./Get-KdsRootKey.md)

[Set-KdsConfiguration](./Set-KdsConfiguration.md)

[测试 KdsRootKey](./Test-KdsRootKey.md)

