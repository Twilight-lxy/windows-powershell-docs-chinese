---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.RemoteAttestation.Server.PowerShell.dll-Help.xml
Module Name: HgsAttestation
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsattestation/add-hgsattestationtpmpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-HgsAttestationTpmPolicy
---

# Add-HgsAttestationTpmPolicy

## 摘要
基于TPM 2.0硬件为HGS添加一个认证策略。

## 语法

### 控制台
```
Add-HgsAttestationTpmPolicy [-InputObject] <Byte[]> -Name <String> [-PolicyVersion <PolicyVersion>] [-Stage]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 文件
```
Add-HgsAttestationTpmPolicy [-Path] <String> [-Name <String>] [-PolicyVersion <PolicyVersion>] [-Stage]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-HgsAttestationTpmPolicy` cmdlet 可将基于可信平台模块（TPM）2.0硬件的认证策略添加到 Host Guardian Service (HGS) 中。请指定一个以 Trusted Computing Group (TCG) 格式生成的日志文件，该日志文件可以通过使用 `Get-HgsAttestationBaselinePolicy` cmdlet 获取。

## 示例

#### 示例 1：添加策略
```
PS C:\> Add-HgsAttestationTpmPolicy -Name "BaselineTpmPolicy17" -Path "C:\Hgs\BaselineTcgLog"
```

该命令向 Attestation 服务添加一个名为 BaselineTpmPolicy17 的策略。Path 参数指定了通过使用 **Get-HgsAttestationBaselinePolicy** cmdlet 创建的 TCG 日志文件。

## 参数

### -InputObject
指定一个以二进制格式存储的TCG日志（Trading Card Game日志），该cmdlet会根据此日志来制定相应的策略。

```yaml
Type: Byte[]
Parameter Sets: Console
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定此 cmdlet 所添加的策略的名称。

```yaml
Type: String
Parameter Sets: Console
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

```yaml
Type: String
Parameter Sets: File
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定一个文件的路径，该文件包含以二进制形式存储的TCG日志。

```yaml
Type: String
Parameter Sets: File
Aliases: FilePath, PSPath

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -PolicyVersion
保留以供将来使用。

```yaml
Type: PolicyVersion
Parameter Sets: (All)
Aliases:
Accepted values: None, PolicyVersion1503, PolicyVersion1704

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Stage
保留以供将来使用。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于常用参数（about_CommonParameters）的文档：http://go.microsoft.com/fwlink/?LinkID=113216。

## 输入

### Byte[], String
这个cmdlet接受一个TCG日志，该日志可以是一个**字节**数组，也可以是一个文件名。

## 输出

### AttestationPolicyInfo
此cmdlet返回身份验证策略信息。

## 备注

## 相关链接

