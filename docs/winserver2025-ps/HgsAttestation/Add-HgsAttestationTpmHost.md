---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.RemoteAttestation.Server.PowerShell.dll-Help.xml
Module Name: HgsAttestation
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsattestation/add-hgsattestationtpmhost?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-HgsAttestationTpmHost
---

# Add-HgsAttestationTpmHost

## 摘要
将一台配备了TPM 2.0技术的受保护主机添加到HGS（Hardware Security Module）中的认证服务中。

## 语法

### 文件
```
Add-HgsAttestationTpmHost [-Name <String>] [-ForeignKey <String>] [-Force] -Path <String>
 [-PolicyVersion <PolicyVersion>] [-Stage] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 控制台
```
Add-HgsAttestationTpmHost [-Name <String>] [-ForeignKey <String>] [-Force] -Xml <XmlDocument>
 [-PolicyVersion <PolicyVersion>] [-Stage] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-HgsAttestationTpmHost` cmdlet 可将受保护的主机添加到 Host Guardian Service (HGS) 中的 Attestation 服务中。要使用此 cmdlet，该主机必须配备支持 Trusted Platform Module (TPM) 2.0 标准的硬件。

## 示例

### 示例 1：添加一个 TPM 主机
```
PS C:\> Add-HgsAttestationTpmHost -Name "TpmHost21" -Path "C:\TpmHost21.xml"
```

此命令将一个 TPM 主机添加到认证服务中。该命令使用由 **Get-PlatformIdentifier** cmdlet 生成的 `.xml` 文件。

## 参数

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

### -ForeignKey
指定一个外键。

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
指定该cmdlet添加到Attestation服务中的受保护主机的友好名称。此主机必须配备TPM 2.0硬件。

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
指定一个.xml文件的完整路径。可以使用**Get-PlatformIdentifier** cmdlet来创建该文件。有关更多信息，请输入`Get-Help Get-PlatformIdentifier`。

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
指定一个包含二进制数据的.xml文件的完整路径。可以使用**Get-PlatformIdentifier**命令来创建该文件。

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

### -Confirm
在运行该 cmdlet 之前，会提示您确认是否要执行该操作。

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
展示了如果运行该cmdlet会发生什么情况。不过实际上这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONPARAMETERS（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

## 输出

### 字符串
这个cmdlet返回一个字符串。

## 备注

## 相关链接

[Get-HgsAttestationTpmHost](./Get-HgsAttestationTpmHost.md)

[Remove-HgsAttestationTpmHost](./Remove-HgsAttestationTpmHost.md)

