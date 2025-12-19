---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/get-iisconfigsection?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IISConfigSection
---

# Get-IISConfigSection

## 摘要
获取一个配置部分对象（configuration section object），以便进一步使用 IIS 配置存储（IIS Configuration Store）。

## 语法

```
Get-IISConfigSection [[-SectionPath] <String>] [[-CommitPath] <String>] [[-Location] <String>]
 [[-Clr] <String>] [<CommonParameters>]
```

## 描述
`Get-IISConfigSection` cmdlet 可以获取一个配置节（`Microsoft.Web.Administration.ConfigurationSection`）对象，以便进一步操作 Internet Information Services (IIS) 的配置存储。当需要读取或更新配置时，这通常是第一个使用的 cmdlet。该 cmdlet 的输出可以传递给管道中的其他需要 `ConfigurationElement` 对象的 cmdlet，因为 `ConfigurationSection` 继承自 `ConfigurationElement`。

如果未使用 *SectionPath* 参数，该 cmdlet 会列出所有可用的部分。这些部分可以在 applicationHost.config（IIS 配置）或根 web.config（.NET Framework）中定义。

## 示例

### 示例 1：获取某个路径对应的配置部分对象
```
PS C:\> $ConfigSection = Get-IISConfigSection -SectionPath "system.applicationHost/sites"
```

这个命令用于获取系统配置中 `applicationHost/sites` 部分的配置对象。

### 示例 2：获取 IIS 网站的进程状态信息
```
PS C:\> $ConfigSection = Get-IISConfigSection -SectionPath "system.applicationHost/sites"
Get-IISConfigCollection $configSection | Get-IISConfigCollectionElement -ConfigAttribute @{"Name"="Default Web Site"} | Get-IISConfigAttributeValue -AttributeName "State"
```

这个命令用于获取默认网站的运行时状态信息。

#### 示例 3：在全局配置级别添加一个新的默认文档
```
PS C:\> Get-IISConfigSection -SectionPath "system.webServer/defaultDocument" | Get-IISConfigCollection -CollectionName "files" | New-IISConfigCollectionElement  -ConfigAttribute @{"Value" = "MyDefDoc.htm"}
```

此命令将文件名 “MyDefDoc.htm” 添加到应用程序配置文件（applicationHost.config）中 `<defaultDocument>` 部分的 `<files>` 目录中。

### 示例 4：创建一个应用程序池
```
PS C:\> Start-IISCommitDelay
PS C:\> $ConfigSectionCollection = Get-IISConfigSection -SectionPath "system.applicationHost/applicationPools" | Get-IISConfigCollection
PS C:\> New-IISConfigCollectionElement -ConfigCollection $configSectionCollection -ConfigAttribute @{"name"="MyNewSiteAppPool"; "autoStart"=$true; "managedPipelineMode"="Integrated" }
PS C:\> Stop-IISCommitDelay
```

这个命令创建了一个应用程序池，并将结果存储在变量 $ConfigSectionCollection 中。

### 示例 5：创建一个集合元素并指定 CLR 版本
```
PS C:\> $collection = Get-IISConfigSection -SectionPath "appSettings" -Clr 2.0
```

这条命令使用“appSettings”作为*SectionPath*来创建一个新的集合元素，并将该元素存储在一个名为$collection的变量中。此外，还使用了*Clr*参数将公共语言运行时（Common Language Runtime）设置为版本2.0。

## 参数

### -Clr
指定 IIS 所引用的 .NET Framework 公共语言运行时（CLR）的版本。如果省略此参数，则会使用默认的 CLR 版本。不过请注意，如果在命令中包含了 *CommitPath* 参数，那么 *Clr* 参数将被忽略，此时将使用相应应用程序池的运行时版本。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 4
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -CommitPath
指定用于获取配置文件的路径。如果省略了 `CommitPath`，则将使用 `applicationHost.config` 或根目录下的 `.NET` 配置文件（即 `root/web.config`）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Location
指定用于返回配置对象的 IIS 配置位置的名称。该名称对应于配置文件中的 `<location>` 标签。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SectionPath
指定要返回配置对象的 IIS 配置节的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONPARAMETERS（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[获取 IISServerManager](./Get-IISServerManager.md)

[适用于 Windows PowerShell 的 IIS 管理 cmdlet](./iisadministration.md)

