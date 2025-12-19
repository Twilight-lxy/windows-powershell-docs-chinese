---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.KeyDistributionService.Cmdlets.dll-Help.xml
Module Name: KDS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/kds/test-kdsrootkey?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-KdsRootKey
---

# Test-KdsRootKey

## 摘要
测试根键配置。

## 语法

```
Test-KdsRootKey [-KeyId] <Guid> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Test-KdsRootKey` cmdlet 用于检测具有指定密钥标识符（ID）的根密钥是否使用有效的配置。该测试会验证新组公钥和新组私钥的生成过程。

此cmdlet有助于根据无效的根密钥配置错误来分析故障情况。

## 示例

### 示例 1：测试根键配置
```
PS C:\> Test-KdsRootKey -KeyId 4A3615F1-5A90-22E4-0B1D-1416F93D4412
```

此命令用于测试由键ID指定的根密钥的配置是否正确。

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

### -KeyId
指定要测试的根密钥的ID。

```yaml
Type: Guid
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无
此cmdlet不接受任何输入对象。

## 输出

### System Boolean
此cmdlet用于判断是否可以使用根密钥来生成派生密钥。

## 备注

## 相关链接

[Add-KdsRootKey](./Add-KdsRootKey.md)

[Clear-KdsCache](./Clear-KdsCache.md)

[Get-KdsConfiguration](./Get-KdsConfiguration.md)

[Set-KdsConfiguration](./Set-KdsConfiguration.md)

[Add-KdsRootKey](./Add-KdsRootKey.md)

