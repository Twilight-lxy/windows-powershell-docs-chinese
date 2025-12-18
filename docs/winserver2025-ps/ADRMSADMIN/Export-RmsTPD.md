---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.RightsManagementServices.Admin.dll-Help.xml
Module Name: ADRMSADMIN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adrmsadmin/export-rmstpd?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-RmsTPD
---

# Export-RmsTPD

## 摘要
将TPD导出到AD RMS中。

## 语法

```
Export-RmsTPD [-SavedFile] <String[]> [-Password] <SecureString> [-V1Compatible] [-Force] [-Path] <String[]>
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Export-RmsTPD` cmdlet 将 Active Directory 权限管理服务 (AD RMS) 中的受信任发布域 (TPD) 导出到一个文件中。

要执行导出操作，请将 *SavedFilePath* 参数设置为导出文件的路径，然后将 *Path* 参数设置为 AD RMS 提供者的路径 `<PSDrive>:\TrustPolicy\TrustedPublishingDomain\<TPD_ID>`，其中 `<PSDrive>` 是提供者驱动器的 ID，`<TPD_ID>` 是您想要导出的 TPD 的 ID。

## 示例

### 示例 1：通过 ID 导出 TPD
```
PS C:\> Export-RmsTPD -Path ".\100" -SavedFile "c:\temp\test.xml"
```

这个命令会将ID为100的TPD数据导出到文件C:\temp\test.xml中。由于没有指定“密码”参数，系统会提示用户输入密码。

#### 示例 2：读取密码并用它来导出 TPD 文件
```
PS C:\> $pswd = Read-Host -AsSecureString
PS C:\> Export-RmsTPD -Path "100" -SavedFile "c:\temp\test.xml" -Password $pswd
```

第一个命令会提示用户输入密码，并将该密码保存在变量 `$pswd` 中。之后，这个变量会被作为 `Password` 参数传递给 `Export-RmsTPD` 命令。需要注意的是，`Export-RmsTPD` 命令还会要求用户再次输入确认密码，该确认密码必须与存储在 `$pswd` 变量中的密码相匹配。

### 示例 3：在不提示输入密码的情况下导出 TPD 文件
```
PS C:\> $pswd=Read-Host -AsSecureString
PS C:\> Export-RmsTPD -Path "100" -SavedFile "c:\temp\test.xml" -Password $pswd -Force
```

第一个命令会要求用户输入密码，并将该密码保存到 `$pswd` 变量中。随后，这个变量作为 `Password` 参数被传递给 `Export-RmsTPD` 命令。由于指定了 `Force` 参数，`Export-RmsTPD` 命令不会再次提示用户输入确认密码。

## 参数

### -Confirm
在运行该cmdlet之前，会提示您确认是否要继续执行该操作。

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

### -Force
如果这些限制不会危及安全性，那么 `Force` 会覆盖那些可能导致命令无法成功执行的限制。例如，`Force` 可以覆盖只读属性或创建目录以完成文件路径的构建，但它不会尝试更改文件的权限。

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
指定一个提供者驱动器及其路径，或者当前驱动器上的相对路径。可以使用点（.）来表示当前位置。此参数不支持通配符，并且没有默认值。

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

### -SavedFile
指定接收导出内容的文件的完整路径和文件名。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -V1Compatible
允许将受信任的发布域导入到 Windows 权限管理服务（RMS）1.0 中。

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

## 输出

## 备注

## 相关链接

[使用 Windows PowerShell 与 AD RMS](https://go.microsoft.com/fwlink/?LinkId=136806)

[Export-RmsTUD](./Export-RmsTUD.md)

[Import-RmsTPD](./Import-RmsTPD.md)

[Import-RmsTUD](./Import-RmsTUD.md)

