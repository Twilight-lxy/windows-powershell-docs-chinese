---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: HgsClient-help.xml
Module Name: HgsClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsclient/new-hgsguardian?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-HgsGuardian
---

# 新版HgsGuardian

## 摘要
创建一个Host Guardian服务守护程序。

## 语法

### 接受证书
```
New-HgsGuardian [-Name] <String> -SigningCertificate <String> [-SigningCertificatePassword <SecureString>]
 -EncryptionCertificate <String> [-EncryptionCertificatePassword <SecureString>] [-AllowExpired]
 [-AllowUntrustedRoot] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 作者：ByThumbprints
```
New-HgsGuardian [-Name] <String> [-AllowExpired] [-AllowUntrustedRoot] -SigningCertificateThumbprint <String>
 -EncryptionCertificateThumbprint <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 生成证书
```
New-HgsGuardian [-Name] <String> [-GenerateCertificates] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`New-HgsGuardian` cmdlet 创建一个称为“Host Guardian Service guardian”的加密实体。这种“guardian”是一个主体（principal），你可以授予它访问存储在密钥保护器（key protector）中的密钥的权限。

## 示例

### 示例 1：创建一个守护者
```
PS C:\> New-HgsGuardian -Name "Guardian11" -GenerateCertificates
```

这个命令创建了一个名为“Guardian11”的Host Guardian Service守护程序。该守护程序可以充当密钥保护器的所有者。由于此命令指定了“GenerateCertificates”参数，因此它会生成签名证书和加密证书。

### 示例 2：使用现有的证书创建一个守护程序（guardian）
```
PS C:\> $SecureStringPassword01 = ConvertTo-SecureString "<Password01>" -AsPlainText -Force
PS C:\> $SecureStringPassword02 = ConvertTo-SecureString "<Password02>" -AsPlainText -Force
PS C:\> New-HgsGuardian -Name "Guardian21" -SigningCertificate "C:\Keys\SigningCertificate.pfx" -SigningCertificatePassword $SecureStringPassword01 -EncryptionCertificate "C:\Keys\EncryptionCertificate.pfx" -EncryptionCertificatePassword $SecureStringPassword02
```

前两个命令使用 **ConvertTo-SecureString** cmdlet 将密码转换成安全的字符串形式。有关更多信息，请输入 `Get-Help ConvertTo-SecureString`。这些命令将生成的密码存储在两个变量中。

最后一条命令创建了一个名为“Guardian21”的守护程序。该命令指定了所需的签名和加密证书，这些证书以受密码保护的.pfx文件形式存在。存储在**$SecureStringPassword01**和**$SecureStringPassword02**中的密码必须与用于生成这些.pfx文件的密码相匹配。

## 参数

### -AllowExpired
表示该cmdlet可以使用已过期的证书来创建守护程序（guardian）。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: AcceptCertificates, ByThumbprints
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AllowUntrustedRoot
表示此cmdlet可以使用自签名证书来创建守护程序（guardian）。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: AcceptCertificates, ByThumbprints
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EncryptionCertificate
指定一个.pfx文件的路径，该文件包含用于保护Guardian的加密证书（该证书使用了密码进行保护）。这个.pfx文件中包含了公钥和私钥。

```yaml
Type: String
Parameter Sets: AcceptCertificates
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EncryptionCertificatePassword
指定用于解密包含加密证书的.pfx文件的密码。

```yaml
Type: SecureString
Parameter Sets: AcceptCertificates
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EncryptionCertificateThumbprint
指定加密证书的指纹（thumbprint）。

```yaml
Type: String
Parameter Sets: ByThumbprints
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GenerateCertificates
这表明该cmdlet会为“守护者”（guardian）生成自签名的签名和加密证书。这些证书包含公钥和私钥。

如果您指定了这个参数，那么新的守护进程将没有受信任的根节点（trusted root）。因此，您还必须指定 **AllowUntrustedRoot** 参数。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: GenerateCertificates
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
为新守护者指定一个名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -SigningCertificate
指定一个.pfx文件的路径，该文件包含用于守护者的、经过密码保护的签名证书。这个.pfx文件中包含了公钥和私钥。

```yaml
Type: String
Parameter Sets: AcceptCertificates
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SigningCertificatePassword
指定用于解密签名证书.pfx文件所需的密码。

```yaml
Type: SecureString
Parameter Sets: AcceptCertificates
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SigningCertificateThumbprint
指定位于本地计算机证书存储库中的签名证书的“指纹”（即该证书的唯一标识信息）。

```yaml
Type: String
Parameter Sets: ByThumbprints
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters (http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### CimInstance#MSFT_HgsGuardian
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名称。

## 备注

## 相关链接

[Export-HgsGuardian](./Export-HgsGuardian.md)

[Get-HgsGuardian](./Get-HgsGuardian.md)

[Import-HgsGuardian](./Import-HgsGuardian.md)

[Remove-HgsGuardian](./Remove-HgsGuardian.md)

