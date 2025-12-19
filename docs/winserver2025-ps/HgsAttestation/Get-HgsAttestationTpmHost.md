---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.RemoteAttestation.Server.PowerShell.dll-Help.xml
Module Name: HgsAttestation
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsattestation/get-hgsattestationtpmhost?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-HgsAttestationTpmHost
---

# 获取 HGS 证书颁发机构 TPM 主机的信息

## 摘要
通过Attestation服务HGS来保护配备了TPM 2.0技术的主机。

## 语法

### NameSet（默认值）
```
Get-HgsAttestationTpmHost [-Name <String>] [-PolicyVersion <PolicyVersion>] [-Stage] [<CommonParameters>]
```

### 文件
```
Get-HgsAttestationTpmHost [-Name <String>] -Path <String> [-PolicyVersion <PolicyVersion>] [-Stage]
 [<CommonParameters>]
```

### 控制台
```
Get-HgsAttestationTpmHost [-Name <String>] -Xml <XmlDocument> [-PolicyVersion <PolicyVersion>] [-Stage]
 [<CommonParameters>]
```

## 描述
`Get-HgsAttestationTpmHost` cmdlet 用于从 Host Guardian Service (HGS) 的 Attestation 服务中检索受保护的主机。该 cmdlet 适用于配备了可信平台模块 (TPM) 2.0 硬件，并且是通过 `Add-HgsAttestationTpmHost` cmdlet 添加的主机。

## 示例

## 参数

### -Name
指定此cmdlet从认证服务（Attestation service）获取的受保护主机的友好名称。

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

### -Path
指定用于获取主机信息的.xml文件的完整路径。可以使用**Get-PlatformIdentifier** cmdlet来创建该文件。有关更多信息，请输入`Get-Help Get-PlatformIdentifier`。

```yaml
Type: String
Parameter Sets: File
Aliases: FilePath

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
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

### -Xml
指定一个.xml文件的完整路径，该文件包含用于获取相关主机信息的二进制数据。可以使用**Get-PlatformIdentifier**命令来创建这个文件。

```yaml
Type: XmlDocument
Parameter Sets: Console
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters (http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### String[]
这个cmdlet返回一个字符串数组。

## 备注

## 相关链接

[Add-HgsAttestationTpmHost](./Add-HgsAttestationTpmHost.md)

[Remove-HgsAttestationTpmHost](./Remove-HgsAttestationTpmHost.md)

