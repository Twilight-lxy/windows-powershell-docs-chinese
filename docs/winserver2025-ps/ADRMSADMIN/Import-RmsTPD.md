---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.RightsManagementServices.Admin.dll-Help.xml
Module Name: ADRMSADMIN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adrmsadmin/import-rmstpd?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Import-RmsTPD
---

# 导入 RMS-TPD

## 摘要
从 AD RMS 中的文件导入一个 TPD（Template Protection Document）。

## 语法

```
Import-RmsTPD [-DisplayName] <String> [-SourceFile] <String> [-Password] <SecureString> [-Force] [-PassThru]
 [-Path] <String[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
**Import-RmsTPD** cmdlet 从 Active Directory 权限管理服务（AD RMS）中的文件导入一个受信任的发布域（TPD）。

要执行导入操作，需要指定 *DisplayName*、*SourceFile* 和 *Password* 参数，然后将 *Path* 参数设置为 AD RMS 提供程序的驱动器路径 `<PSDrive>:\TrustPolicy\TrustedPublishingDomain`，其中 `<PSDrive>` 是提供程序驱动器的 ID。

## 示例

### 示例 1：导入一个 TPD 并为其指定名称
```
PS C:\> Import-RmsTPD -Path "." -DisplayName "Fabrikam" -SourceFile "c:\transfer\fabrikam.xml"
```

此命令导入存储在指定文件中的 TPD 信息，并将 “Fabrikam” 这个名称分配给该 TPD。由于没有指定 “Password” 参数，因此 **Import-RmsTPD** cmdlet 会提示用户输入域密码。

### 示例 2：读取密码并使用该密码导入 TPD 文件
```
PS C:\> $pswd = Read-Host -Prompt "Password:" -AsSecureString
PS C:\> Import-RmsTPD -Path "." -DisplayName "Fabrikam" -SourceFile "c:\transfer\fabrikam.xml" -Password $pswd
```

该命令使用 **Read-Host** cmdlet 来提示用户输入密码，然后将密码存储在一个变量中，该变量会被传递给 **Import-RmsTPD** cmdlet。

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

### -DisplayName
指定用于识别所导入域的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Force
绕过那些会阻止命令成功的限制措施，只是为了确保所做的更改不会危及安全性。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -PassThru
将该cmdlet创建的对象传递到管道中。默认情况下，该cmdlet不会向管道中传递任何对象。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Password
将密码指定为一个 **SecureString** 对象。要创建一个包含密码的 **SecureString** 对象，可以使用 Read-Host cmdlet 并指定 *AsSecureString* 参数。

```yaml
Type: SecureString
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Path
指定一个提供程序驱动器及其路径，或者是当前驱动器上的相对路径。可以使用点（.）来表示当前位置。此参数不支持通配符，且没有默认值。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SourceFile
指定包含要导入的域名信息的文件的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.RightsManagementServices.PowerShell.TrustedPublishingDomainImportedItem

## 备注

## 相关链接

[使用 Windows PowerShell 与 AD RMS](https://go.microsoft.com/fwlink/?LinkId=136806)

[Export-RmsTPD](./Export-RmsTPD.md)

